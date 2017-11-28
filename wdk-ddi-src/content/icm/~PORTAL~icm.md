# Icm.h header


This header is used by unknown technology.

Icm.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WcsAssociateColorProfileWithDevice function](nf-icm-wcsassociatecolorprofilewithdevice.md) | The WcsAssociateColorProfileWithDevice function associates a specified WCS color profile with a specified device. |
| [WcsCheckColors function](nf-icm-wcscheckcolors.md) | The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform. |
| [WcsCreateIccProfile function](nf-icm-wcscreateiccprofile.md) | The WcsCreateIccProfile function converts a WCS profile into an ICC profile. |
| [WcsDisassociateColorProfileFromDevice function](nf-icm-wcsdisassociatecolorprofilefromdevice.md) | The WcsDisassociateColorProfileFromDevice function disassociates a specified WCS color profile from a specified device. |
| [WcsEnumColorProfiles function](nf-icm-wcsenumcolorprofiles.md) | The WcsEnumColorProfiles function enumerates all color profiles that satisfy the enumeration criteria in the specified profile management scope. |
| [WcsEnumColorProfilesSize function](nf-icm-wcsenumcolorprofilessize.md) | The WcsEnumColorProfilesSize function returns the size, in bytes, of the buffer required by the WcsEnumColorProfiles function to enumerate color profiles. |
| [WcsGetDefaultColorProfile function](nf-icm-wcsgetdefaultcolorprofile.md) | The WcsGetDefaultColorProfile function retrieves the default color profile for a device, or the device-independent default if the device is not specified. |
| [WcsGetDefaultColorProfileSize function](nf-icm-wcsgetdefaultcolorprofilesize.md) | The WcsGetDefaultColorProfileSize function returns the size, in bytes, of the default color profile name for a device, including the NULL terminator. |
| [WcsGetUsePerUserProfiles function](nf-icm-wcsgetuseperuserprofiles.md) | The WcsGetUsePerUserProfiles function determines whether the user has chosen to use a per-user profile association list for the specified device. |
| [WcsSetDefaultColorProfile function](nf-icm-wcssetdefaultcolorprofile.md) | The WcsSetDefaultColorProfile function sets the default color profile name of the specified profile type in the specified profile management scope. |
| [WcsSetUsePerUserProfiles function](nf-icm-wcssetuseperuserprofiles.md) | The WcsSetUsePerUserProfiles function allows the user to specify whether or not to use a per-user profile association list for the specified device. |
| [WcsTranslateColors function](nf-icm-wcstranslatecolors.md) | The WcsTranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BMFORMAT enumeration](ne-icm-bmformat.md) | The values of the BMFORMAT enumeration are used by WCS functions to indicate the format that particular bitmaps are in. This data type is extended from BMFORMAT that is available in versions of Windows released before Windows Vista. |
| [COLORDATATYPE enumeration](ne-icm-colordatatype.md) | The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content. |
| [COLORPROFILESUBTYPE enumeration](ne-icm-colorprofilesubtype.md) | The COLORPROFILESUBTYPE enumeration is used to specify the subtype of color profile. |
| [COLORPROFILETYPE enumeration](ne-icm-colorprofiletype.md) | The COLORPROFILETYPE enumeration is used to specify the type of color profile. |
| [COLORTYPE enumeration](ne-icm-colortype.md) | The values of the COLORTYPE enumeration are used by WCS functions to indicate the format of vector content. Most values have equivalent structures that are contained in the ICM COLOR structure (described in the Microsoft Windows SDK documentation). |
| [WCS_PROFILE_MANAGEMENT_SCOPE enumeration](ne-icm-wcs-profile-management-scope.md) | The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device. |
