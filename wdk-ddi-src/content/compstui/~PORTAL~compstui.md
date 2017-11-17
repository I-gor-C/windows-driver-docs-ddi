# Declarations in the compstui header
This header Compstui contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [PPSPINFO_FROM_WM_INITDIALOG_LPARAM function](nf-compstui-ppspinfo-from-wm-initdialog-lparam.md) | TBD |
| [SetCPSUIUserData function](nf-compstui-setcpsuiuserdata.md) | CPSUI's SetCPSUIUserData function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box. |
| [CommonPropertySheetUIA function](nf-compstui-commonpropertysheetuia~r1.md) | TBD |
| [GetCPSUIUserData function](nf-compstui-getcpsuiuserdata.md) | CPSUI's GetCPSUIUserData function retrieves data that was previously stored using the SetCPSUIUserData function. |
| [CommonPropertySheetUIA function](nf-compstui-commonpropertysheetuia.md) | TBD |
| [IS_DMPUB_HIDDEN function](nf-compstui-is-dmpub-hidden.md) | TBD |
| [CommonPropertySheetUIW function](nf-compstui-commonpropertysheetuiw.md) | TBD |
| [MAKE_DMPUB_HIDEBIT function](nf-compstui-make-dmpub-hidebit.md) | TBD |
| [CommonPropertySheetUIW function](nf-compstui-commonpropertysheetuiw~r1.md) | TBD |
| [HINSPSUIPAGE_INDEX function](nf-compstui-hinspsuipage-index.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNCOMPROPSHEET callback function](nc-compstui-pfncompropsheet.md) | TBD |
| [_CPSUICALLBACK callback function](nc-compstui--cpsuicallback.md) | TBD |
| [PFNPROPSHEETUI callback function](nc-compstui-pfnpropsheetui.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SETRESULT_INFO structure](ns-compstui--setresult-info.md) | The SETRESULT_INFO structure is used as an input parameter to an application's PFNPROPSHEETUI-typed callback function. |
| [OIEXT structure](ns-compstui--oiext.md) | The OIEXT structure supplies additional, optional information about a property sheet page option that is described by an OPTITEM structure. |
| [EXTCHKBOX structure](ns-compstui--extchkbox.md) | The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option. |
| [DLGPAGE structure](ns-compstui--dlgpage.md) | The DLGPAGE structure is used for specifying a property sheet page to CPSUI's ComPropSheet function. The structure's address is included in a COMPROPSHEETUI structure, and all member values are supplied by the ComPropSheet caller. |
| [PSPINFO structure](ns-compstui--pspinfo.md) | The PSPINFO structure is used as an input parameter to a property sheet page's dialog box procedure, when the Windows message is WM_INITDIALOG. The dialog box procedure's address is specified in a DLGPAGE structure. |
| [OPTPARAM structure](ns-compstui--optparam.md) | An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a property sheet option. The array's address is included in an OPTTYPE structure. |
| [COMPROPSHEETUI structure](ns-compstui--compropsheetui.md) | The COMPROPSHEETUI structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_ADD_PCOMPROPSHEETUI. All structure members must be supplied by the caller of ComPropSheet. |
| [PROPSHEETUI_INFO structure](ns-compstui--propsheetui-info.md) | The PROPSHEETUI_INFO structure is used as an input parameter to PFNPROPSHEETUI-typed functions. |
| [PROPSHEETUI_INFO_HEADER structure](ns-compstui--propsheetui-info-header.md) | The PROPSHEETUI_INFO_HEADER structure is used as an input parameter to an application's PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_INFO_HEADER. |
| [OPTTYPE structure](ns-compstui--opttype.md) | The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a property sheet option, if the option is specified by an OPTITEM structure. |
| [CPSUIDATABLOCK structure](ns-compstui--cpsuidatablock.md) | The CPSUIDATABLOCK structure is used as a parameter for the ComPropSheet function, if the function code is CPSFUNC_SET_DATABLOCK or CPSFUNC_QUERY_DATABLOCK. |
| [EXTPUSH structure](ns-compstui--extpush.md) | The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed. |
| [OPTCOMBO structure](ns-compstui--optcombo.md) | TBD. |
| [PROPSHEETUI_GETICON_INFO structure](ns-compstui--propsheetui-geticon-info.md) | The PROPSHEETUI_GETICON_INFO structure is used as an input parameter to an application's PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_ICON. |
| [INSERTPSUIPAGE_INFO structure](ns-compstui--insertpsuipage-info.md) | The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_INSERT_PSUIPAGE. All member values must be supplied by the ComPropSheet caller. |
| [OPTITEM structure](ns-compstui--optitem.md) | The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one property sheet option on a property sheet page, if the page is described by a COMPROPSHEETUI structure. |
| [CPSUICBPARAM structure](ns-compstui--cpsuicbparam.md) | The CPSUICBPARAM structure is used as the input parameter to _CPSUICALLBACK-typed callback functions. |

This header is used in these topics:

- [print](..content/_print)
