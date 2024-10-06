def map_and_format_row(row, header, mapping):
    target_header = [
        "type",
        "product_internal_id",
        "product_sku",
        "product_name",
        "product_price",
        "product_compare_to_price",
        "product_is_inventory_tracked",
        "product_quantity",
        "product_quantity_out_of_stock_behaviour",
        "product_low_stock_notification_quantity",
        "product_quantity_minimum_allowed_for_purchase",
        "product_quantity_maximum_allowed_for_purchase",
        "product_is_available",
        "product_media_main_image_url",
        "product_media_main_image_alt",
        "product_media_gallery_image_url_1",
        "product_media_gallery_image_alt_1",
        "product_media_gallery_image_url_2",
        "product_media_gallery_image_alt_2",
        "product_description",
        "product_category_1",
        "product_category_2",
        "product_category_3",
        "product_is_featured",
        "product_is_featured_order_by",
        "product_brand",
        "product_upc",
        "product_weight",
        "product_is_shipping_required",
        "product_length",
        "product_width",
        "product_height",
        "product_shipping_preparation_time_for_shipping_in_days",
        "product_shipping_preparation_time_for_pickup_in_minutes",
        "product_shipping_preparation_time_for_local_delivery_in_minutes",
        "product_shipping_preparation_time_for_preorders_in_days",
        "product_shipping_show_delivery_date_on_the_product_page",
        "product_tax_class_code",
        "product_seo_title",
        "product_seo_description",
        "product_related_item_ids",
        "product_related_item_skus",
        "product_related_items_random",
        "product_related_items_random_category",
        "product_related_items_random_number_of_items",
        "product_custom_price_enabled",
        "product_subscription_enabled",
        "product_subscription_one_time_purchase_enabled",
        "product_subscription_one_time_purchase_price",
        "product_subscription_price_with_signup_fee",
        "product_subscription_recurring_interval",
        "product_subscription_recurring_interval_count",
        "product_google_product_category_code",
        "product_option_name",
        "product_option_type",
        "product_option_is_required",
        "product_option_value",
        "product_option_markup",
        "product_option_is_default_option_selection",
        "category_internal_id",
        "category_path",
        "category_is_available",
        "category_description",
        "category_seo_title",
        "category_seo_description",
        "category_image",
        "category_image_alt",
        "category_order_by",
        "source_store_id",
        "url",
    ]

    header_mapping = {
        "sku": "product_sku",
        "name": "product_name",
        "price": "product_price",
        "description": "product_description",
    }

    mapped_row = []
    for target_col in target_header:
        if target_col in header_mapping:
            source_col = list(mapping.keys())[list(mapping.values()).index(target_col)]
            if source_col in header:
                mapped_row.append(row[header.index(source_col)])
            else:
                mapped_row.append("")
        else:
            mapped_row.append("")
    return mapped_row
