# mkogp

mkogp generates OGP-image automatically.

You can use this in an environment using a template engine such as Jekyll.

Set three environment variables.

```bash
EXPORT_PATH=assets/ogp
POSTS_PATH=_posts
BLOG_TITLE=shimewtrのブログ
```

Place your profile icon in `assets/icon.png`.

Generates OGP-image for the file in the folder specified by `POST_PATH`.

Please include the following information at the top of the file.

```yaml
---
title: "Article Title"
ogp: ogp
---
```

The value of `ogp` is the name of the image file to be generated.

The generated image is output to `EXPORT_PATH`.

The generated image looks like this.

![sample_image](https://github.com/shimewtr/mkogp/blob/master/assets/ogp/ogp.png?raw=true,"sample_image")

## License

mkogp is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

M PLUS 1p fonts are licensed under the [SIL Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL).
