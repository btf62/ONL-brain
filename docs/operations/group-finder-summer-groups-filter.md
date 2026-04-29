# Group Finder Summer Groups Filter

## Purpose

The Community Groups Group Finder page has a seasonal `Summer Group` filter. This filter is turned on when summer groups are available and turned off when the summer group season is over.

This is controlled from the Group Finder block settings on the Community Groups page in Rock RMS.

## Page

- Public page: `/groupfinder`
- Page title: `Community Groups`
- Block configuration: `Group Finder Configuration`

## When To Turn It On

Turn on the `Summer Group` filter when summer groups should be discoverable on the Community Groups Group Finder page.

This usually happens before or during the summer group promotion window.

## When To Turn It Off

Turn off the `Summer Group` filter when summer groups are no longer being promoted or should no longer appear as a public seasonal filter.

This usually happens after the summer group season ends.

## Turn The Summer Group Filter On

1. Log in to Rock with access to edit the Community Groups Group Finder page.
2. Go to `/groupfinder`.
3. Open the block settings for the Group Finder block.
4. In `Group Finder Configuration`, find `Display Attribute Filters`.
5. Check `Summer Group (Community Group)`.
6. Save the block settings.
7. Refresh `/groupfinder`.
8. Confirm the `Summer Group` filter appears on the Community Groups search form.
9. Test the filter by searching with summer groups enabled.

## Turn The Summer Group Filter Off

1. Log in to Rock with access to edit the Community Groups Group Finder page.
2. Go to `/groupfinder`.
3. Open the block settings for the Group Finder block.
4. In `Group Finder Configuration`, find `Display Attribute Filters`.
5. Uncheck `Summer Group (Community Group)`.
6. Save the block settings.
7. Refresh `/groupfinder`.
8. Confirm the `Summer Group` filter no longer appears on the Community Groups search form.

## Validation

After changing the setting, verify the public page behavior:

- When enabled, the filter area includes `Summer Group`.
- When disabled, the filter area does not include `Summer Group`.
- Existing standard filters such as campus, stage of life, meeting type, childcare, meets on, and Deaf/HOH friendly still appear as expected.
- Group search still loads results and the map normally.

## Notes

The `Summer Group` filter is only a seasonal display setting on the Group Finder block. Avoid changing unrelated block settings while turning this filter on or off.
