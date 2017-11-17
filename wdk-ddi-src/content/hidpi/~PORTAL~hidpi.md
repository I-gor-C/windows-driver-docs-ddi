# Declarations in the hidpi header
This header Hidpi contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HIDP_KEYBOARD_DIRECTION enumeration](ne-hidpi--hidp-keyboard-direction.md) | TBD |
| [HIDP_REPORT_TYPE enumeration](ne-hidpi--hidp-report-type.md) | The HIDP_REPORT_TYPE enumeration type is used to specify a HID report type. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidP_GetLinkCollectionNodes function](nf-hidpi-hidp-getlinkcollectionnodes.md) | The HidP_GetLinkCollectionNodes routine returns a top-level collection's link collection array. |
| [HidP_GetUsages function](nf-hidpi-hidp-getusages.md) | The HidP_GetUsages routine returns a list of all the HID control button usages that are on a specified usage page and are set to ON in a HID report. |
| [HidP_GetCaps function](nf-hidpi-hidp-getcaps.md) | The HidP_GetCaps routine returns a top-level collection's HIDP_CAPS structure. |
| [HidP_GetButtonCaps function](nf-hidpi-hidp-getbuttoncaps.md) | The HidP_GetButtonCaps routine returns a button capability array that describes all the HID control buttons in a top-level collection for a specified type of HID report. |
| [HidP_SetUsages function](nf-hidpi-hidp-setusages.md) | The HidP_SetUsages routine sets specified HID control buttons ON (1) in a HID report. |
| [HidP_GetValueCaps function](nf-hidpi-hidp-getvaluecaps.md) | The HidP_GetValueCaps routine returns a value capability array that describes all the HID control values in a top-level collection for a specified type of HID report. |
| [HidP_GetExtendedAttributes function](nf-hidpi-hidp-getextendedattributes.md) | The HidP_GetExtendedAttributes routine returns the extended attributes of a HID control. |
| [HidP_SetUsageValue function](nf-hidpi-hidp-setusagevalue.md) | The HidP_SetUsageValue routine sets a HID control value in a specified HID report. |
| [HidP_GetUsageValue function](nf-hidpi-hidp-getusagevalue.md) | The HidP_GetUsageValue routine extracts the data associated with a HID control value that matches the selection criteria in a HID report. |
| [HIDP_ERROR_CODES function](nf-hidpi-hidp-error-codes.md) | TBD |
| [HidP_IsSameUsageAndPage function](nf-hidpi-hidp-issameusageandpage.md) | TBD |
| [HidP_UnsetUsages function](nf-hidpi-hidp-unsetusages.md) | The HidP_UnsetUsages routine sets specified HID control button usages OFF (zero) in a HID report. |
| [HidP_GetData function](nf-hidpi-hidp-getdata.md) | The HidP_GetData routine returns, for a specified report, an array of HIDP_DATA structures that identify the data indices of all HID control buttons that are currently set to ON (1), and the data indices and data associated with all HID control values. |
| [HidP_GetSpecificButtonCaps function](nf-hidpi-hidp-getspecificbuttoncaps.md) | The HidP_GetSpecificButtonCaps routine returns a button capability array that describes all HID control buttons in a top-level collection that meet a specified selection criteria. |
| [HidP_TranslateUsagesToI8042ScanCodes function](nf-hidpi-hidp-translateusagestoi8042scancodes.md) | The HidP_TranslateUsagesToI8042ScanCodes routine maps a list of HID usages on the HID_USAGE_PAGE_KEYBOARD usage page to their respective PS/2 scan codes (Scan Code Set 1). |
| [HidP_SetUsageValueArray function](nf-hidpi-hidp-setusagevaluearray.md) | The HidP_SetUsageValueArray routine sets a HID control usage value array in a specified HID report. |
| [HidP_UsageListDifference function](nf-hidpi-hidp-usagelistdifference.md) | The HidP_UsageListDifference routine returns the differences between two arrays of HID usages. |
| [HidP_UnsetButtons function](nf-hidpi-hidp-unsetbuttons.md) | TBD |
| [HidP_UsageAndPageListDifference function](nf-hidpi-hidp-usageandpagelistdifference.md) | TBD |
| [HidP_SetScaledUsageValue function](nf-hidpi-hidp-setscaledusagevalue.md) | The HidP_SetScaledUsageValue routine converts a signed and scaled physical number to a HID usage's logical value, and sets the usage value in a specified HID report. |
| [HidP_MaxUsageListLength function](nf-hidpi-hidp-maxusagelistlength.md) | The HidP_MaxUsageListLength routine returns the maximum number of HID usages that HidP_GetUsages can return for a specified type of HID report and a specified top-level collection. |
| [HidP_GetScaledUsageValue function](nf-hidpi-hidp-getscaledusagevalue.md) | The HidP_GetScaledUsageValue routine returns the signed and scaled result of a HID control value extracted from a HID report. |
| [HidP_SetButtons function](nf-hidpi-hidp-setbuttons.md) | TBD |
| [HidP_MaxDataListLength function](nf-hidpi-hidp-maxdatalistlength.md) | The HidP_MaxDataListLength routine returns the maximum number of HIDP_DATA structures that HidP_GetData can return for a specified type of HID report and a specified top-level collection. |
| [HidP_GetButtonsEx function](nf-hidpi-hidp-getbuttonsex.md) | TBD |
| [HidP_InitializeReportForID function](nf-hidpi-hidp-initializereportforid.md) | The HidP_InitializeReportForID routine initializes a HID report. |
| [HidP_SetData function](nf-hidpi-hidp-setdata.md) | The HidP_SetData routine sets a specified set of HID control button and value usages in a HID report. |
| [HidP_GetUsageValueArray function](nf-hidpi-hidp-getusagevaluearray.md) | The HidP_GetUsageValueArray routine extracts the data associated with a HID control usage value array from a HID report. |
| [HidP_TranslateUsageAndPagesToI8042ScanCodes function](nf-hidpi-hidp-translateusageandpagestoi8042scancodes.md) | TBD |
| [HidP_GetUsagesEx function](nf-hidpi-hidp-getusagesex.md) | The HidP_GetUsagesEx routine returns a list of the all the HID control button usages that are set to ON in a HID report. |
| [HidP_GetSpecificValueCaps function](nf-hidpi-hidp-getspecificvaluecaps.md) | The HidP_GetSpecificValueCaps routine returns a value capability array that describes all HID control values that meet a specified selection criteria. |
| [HidP_GetButtons function](nf-hidpi-hidp-getbuttons.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PHIDP_INSERT_SCANCODES callback function](nc-hidpi-phidp-insert-scancodes.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HIDP_KEYBOARD_MODIFIER_STATE structure](ns-hidpi--hidp-keyboard-modifier-state.md) | TBD |
| [USAGE_AND_PAGE structure](ns-hidpi--usage-and-page.md) | The USAGE_AND_PAGE structure specifies the usage page and usage ID of a HID control. |
| [HIDP_VALUE_CAPS structure](ns-hidpi--hidp-value-caps.md) | The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a usage range). |
| [HIDP_PREPARSED_DATA structure](ns-hidpi--hidp-preparsed-data.md) | TBD |
| [HIDP_DATA structure](ns-hidpi--hidp-data.md) | The HIDP_DATA structure contains information about a HID control's data index and value in a HID report. |
| [HIDP_CAPS structure](ns-hidpi--hidp-caps.md) | The HIDP_CAPS structure contains information about a top-level collection's capability. |
| [HIDP_BUTTON_CAPS structure](ns-hidpi--hidp-button-caps.md) | The HIDP_BUTTON_CAPS structure contains information about the capability of a HID control button usage (or a set of buttons associated with a usage range). |
| [HIDP_EXTENDED_ATTRIBUTES structure](ns-hidpi--hidp-extended-attributes.md) | The HIDP_EXTENDED_ATTRIBUTES structure contains information about the global items specified for a HID control that the HID parser did not recognize. |
| [HIDP_UNKNOWN_TOKEN structure](ns-hidpi--hidp-unknown-token.md) | The HIDP_UNKNOWN_TOKEN structure contains information about a global item that the HID parser did not recognize. |
| [HIDP_LINK_COLLECTION_NODE structure](ns-hidpi--hidp-link-collection-node.md) | The HIDP_LINK_COLLECTION_NODE structure contains information about a link collection in a top-level collection's link collection array. |

This header is used in these topics:

- [hid](..content/_hid)
