import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';


export async function GET(context) {
    const posts = await getCollection('posts');
    const ruPosts = posts.filter(p => p.id.split('/')[1] === 'ru' && !p.data.hidden);
    return rss({
        title: 'Python Sucks',
        description: 'Почему Python так хорош?',
        site: context.site,
        items: ruPosts.map((post) => {
            const [cat, , slug] = post.id.split('/');
            return {
                title: post.data.title,
                pubDate: post.data.pubDate,
                description: post.data.description,
                link: `/posts/${cat}/${slug}/`,
            };
        }),
    });
}
