from .routes import NAV_ITEMS, BRAND_ROUTE


def full_route_list_from_tree(top):
    if "subitems" in top:
        subitems = top["subitems"]
        sub_sub_routes = [subitem["sub_sub_items"] for subitem in subitems if "sub_sub_items" in subitem]
        return sum(sub_sub_routes, subitems + [top])
    else:
        return [top]


def all_routes_and_subroutes():
    full_list = full_route_list_from_tree(BRAND_ROUTE)
    for item in NAV_ITEMS:
        full_list += full_route_list_from_tree(item)
    return full_list


def get_page_title_for_route(route):
    return [
        # TODO: Check what's going on here with routes
        nav["title"] for nav in all_routes_and_subroutes() if "route" in nav and nav["route"] == route
    ][0]


def get_subitems_for_route(route):
    return [nav for nav in NAV_ITEMS if nav["route"] == route][0]["subitems"]
