import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';


export async function GET(context) {
    const posts = await getCollection('posts');
    const enPosts = posts.filter(p => p.id.split('/')[1] === 'en');
    return rss({
        title: 'Python Sucks',
        description: 'Why is Python so great?',
        site: context.site,
        items: enPosts.map((post) => {
            const [cat, , slug] = post.id.split('/');
            return {
                title: post.data.title,
                pubDate: post.data.pubDate,
                description: post.data.description,
                link: `/en/posts/${cat}/${slug}/`,
            };
        }),
    });
}
