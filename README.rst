=====
rich-content-blocks
=====

Todo...

Quick start
-----------
1. Follow configuration instructions for ckeditor_ (skip this step if ckeditor is already configured).

2. Run migrations:: 

    manage.py migrate

3. Add "richcontent" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'richcontentblocks',
    )

You should now have an admin tool with the ability to create rich content blocks.

Using in template
------------------
An example of loading a rich content block, with a key 'my-block' in a template::

    {% load rich_content_block_tags %}
    <div>
        the content block will be in next div
    </div>
    <div>
        {% rich_content_block 'my-block' %}
    </div>


.. _ckeditor: https://github.com/django-ckeditor/django-ckeditor