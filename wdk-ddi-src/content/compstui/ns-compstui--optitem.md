---
UID: NS.compstui._OPTITEM
title: OPTITEM
author: windows-driver-content
description: The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one property sheet option on a property sheet page, if the page is described by a COMPROPSHEETUI structure.
old-location: print\optitem.htm
old-project: print
ms.assetid: 983f9774-d498-473a-bdfb-ec55cc4298cf
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: OPTITEM, OPTITEM, *POPTITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPTITEM
req.alt-loc: compstui.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# OPTITEM structure



## -description
<p>The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one <a href="https://msdn.microsoft.com/572330d6-1a1b-46fd-bfb4-be2b0990bca4">property sheet option</a> on a property sheet page, if the page is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>


## -syntax

````
typedef struct _OPTITEM {
  WORD      cbSize;
  BYTE      Level;
  BYTE      DlgPageIdx;
  DWORD     Flags;
  ULONG_PTR UserData;
  LPTSTR    pName;
  union {
    LONG   Sel;
    LPTSTR pSel;
  };
  union {
    PEXTCHKBOX pExtChkBox;
    PEXTPUSH   pExtPush;
  };
  POPTTYPE  pOptType;
  DWORD     HelpIndex;
  BYTE      DMPubID;
  BYTE      UserItemID;
  WORD      wReserved;
  POIEXT    pOIExt;
  ULONG_PTR dwReserved[3];
} OPTITEM, *POPTITEM;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Size, in bytes, of the OPTITEM structure.</p>
</dd>

### -field <b>Level</b>

<dd>
<p>Specifies the level of this option in the treeview. For more information, see the following Remarks section.</p>
</dd>

### -field <b>DlgPageIdx</b>

<dd>
<p>Identifies the dialog to which the option belongs. Specifies an array index into the DLGPAGE array pointed to by the <b>pDlgPage</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>
<p>If <b>pDlgPage</b> points to a CPSUI-supplied, predefined DLGPAGE structure, CPSUI supplies this index.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Optional bit flags that modify the option's characteristics. The OPTIF_CHANGEONCE flag is set by CPSUI; all other flags are set by the caller. Any combination of the following flags can be set.</p>
<p></p>
<dl>

### -field <a id="OPTIF_CALLBACK"></a><a id="optif_callback"></a>OPTIF_CALLBACK

<dd>
<p>When a user modifies the option, CPSUI should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_CHANGED"></a><a id="optif_changed"></a>OPTIF_CHANGED

<dd>
<p>The <b>_CPSUICALLBACK</b>-typed callback function should set this flag if it modified the option, so that CPSUI will redisplay it.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_CHANGEONCE"></a><a id="optif_changeonce"></a>OPTIF_CHANGEONCE

<dd>
<p>CPSUI sets this bit if a user modified the option.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_COLLAPSE"></a><a id="optif_collapse"></a>OPTIF_COLLAPSE

<dd>
<p>Collapse this option and its children so that it is not expanded in the treeview.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_DISABLED"></a><a id="optif_disabled"></a>OPTIF_DISABLED

<dd>
<p>Disables the option so that it is not user-modifiable.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_ECB_CHECKED"></a><a id="optif_ecb_checked"></a>OPTIF_ECB_CHECKED

<dd>
<p>The associated extended check box is in the checked state.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_EXT_IS_EXTPUSH"></a><a id="optif_ext_is_extpush"></a>OPTIF_EXT_IS_EXTPUSH

<dd>
<p>If set, the <b>pExtPush</b> member is valid (unless <b>NULL</b>).</p>
<p>If not set, the <b>pExtChkBox</b> member is valid (unless <b>NULL</b>).</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_EXT_DISABLED"></a><a id="optif_ext_disabled"></a>OPTIF_EXT_DISABLED

<dd>
<p>The extended check box or extended push button is not selectable.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_EXT_HIDE"></a><a id="optif_ext_hide"></a>OPTIF_EXT_HIDE

<dd>
<p>CPSUI will not display the extended check box or extended push button.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_HAS_POIEXT"></a><a id="optif_has_poiext"></a>OPTIF_HAS_POIEXT

<dd>
<p>If set, the <b>pOIExt</b> member is valid.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_HIDE"></a><a id="optif_hide"></a>OPTIF_HIDE

<dd>
<p>CPSUI will not display this option in the treeview. CPSUI examines this flag only when initially creating the treeview, so changing the flag from its initial value has no effect.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="_OPTIF_INITIAL_TVITEM"></a><a id="_optif_initial_tvitem"></a> OPTIF_INITIAL_TVITEM

<dd>
<p>If set, CPSUI sets the initial window focus to this option when it displays the treeview. CPSUI expands tree nodes and scrolls the option into view as necessary. If the option is hidden, or if this flag is not set for any OPTITEM structure, CPSUI chooses the initial focus.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_NO_GROUPBOX_NAME"></a><a id="optif_no_groupbox_name"></a>OPTIF_NO_GROUPBOX_NAME

<dd>
<p>If not set, and <b>pOptype</b> is not zero, CPSUI uses the <b>pName</b> string as the groupbox title.</p>
<p>If set, CPSUI provides a groupbox title.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_OVERLAY_NO_ICON"></a><a id="optif_overlay_no_icon"></a>OPTIF_OVERLAY_NO_ICON

<dd>
<p>If set CPSUI overlays its IDI_CPSUI_NO icon onto the icon associated with the option. (See the <b>Sel/pSel</b> member.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_OVERLAY_STOP_ICON"></a><a id="optif_overlay_stop_icon"></a>OPTIF_OVERLAY_STOP_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_STOP icon onto the icon associated with the option. (See the <b>Sel/pSel</b> member.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_OVERLAY_WARNING_ICON"></a><a id="optif_overlay_warning_icon"></a>OPTIF_OVERLAY_WARNING_ICON

<dd>
<p>If set, CPSUI overlays its IDI_CPSUI_WARNING icon onto the icon associated with the option. (See the <b>Sel/pSel</b> member.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="OPTIF_SEL_AS_HICON"></a><a id="optif_sel_as_hicon"></a>OPTIF_SEL_AS_HICON

<dd>
<p>If set, the <b>Sel</b> member contains an icon handle.</p>
<p>If not set, the <b>Sel</b> member contains an icon resource identifier.</p>
<p>This flag can only be used when <b>pOptType</b> contains <b>NULL</b>.</p>
</dd>
</dl>
</dd>

### -field <b>UserData</b>

<dd>
<p>Optional 32-bit value that can be set and used by the caller.</p>
<p>(Printer interface DLLs for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> and <a href="wdkgloss.p#wdkgloss.pscript#wdkgloss.pscript"><i>Pscript</i></a> use this member to supply a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563611">USERDATA</a> structure. <a href="NULL">User interface plug-ins</a> can reference this structure.)</p>
</dd>

### -field <b>pName</b>

<dd>
<p>String identifier representing a localized, displayable option name. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier, with HIWORD set to zero. (Also see the description of <b>DMPubID</b>, below.)</p>
</dd>

### -field <b>Sel</b>

<dd>
<p>This union indicates the option's currently selected parameter value. Its usage is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
<p>If <b>pOptType</b> is <b>NULL</b>, the option has no parameters, so this union identifies an icon to be associated with the treeview node for the option. The icon identifier can be either an icon handle or an icon resource identifier, as indicated by OPTIF_SEL_AS_HICON in <b>Flags</b>.</p>
</dd>

### -field <b>pSel</b>

<dd>
<p>This union indicates the option's currently selected parameter value. Its usage is dependent on the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a>.</p>
<p>If <b>pOptType</b> is <b>NULL</b>, the option has no parameters, so this union identifies an icon to be associated with the treeview node for the option. The icon identifier can be either an icon handle or an icon resource identifier, as indicated by OPTIF_SEL_AS_HICON in <b>Flags</b>.</p>
</dd>

### -field <b>pExtChkBox</b>

<dd>
<p>Pointer to EXTCHKBOX structure</p>
</dd>

### -field <b>pExtPush</b>

<dd>
<p>This union can be a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548781">EXTCHKBOX</a> structure, a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a> structure, or <b>NULL</b>.</p>
<p>An OPTITEM structure can optionally have an EXTCHKBOX structure, an EXTPUSH structure, or neither, associated with it. If this union is not <b>NULL</b>, and if OPTIF_EXT_IS_EXTPUSH is set in <b>Flags</b>, <b>pExtPush</b> is valid. If the flag is not set, <b>pExtChkBox</b> is valid.</p>
</dd>

### -field <b>pOptType</b>

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559670">OPTTYPE</a> structure that describes the option's display type. If <b>NULL</b>, the option has no parameters and is used as a parent to options with a higher <b>Level</b> value. The child options must immediately follow the parent in the OPTITEM array. (See the following Remarks section.)</p>
</dd>

### -field <b>HelpIndex</b>

<dd>
<p>Help file index, which identifies help text to be associated with the option. If zero, help file text does not exist for this option. Note that the <b>pOIExt</b> member of this structure must be set with the address of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559590">OIEXT</a> structure in order for help text functionality to exist.</p>
</dd>

### -field <b>DMPubID</b>

<dd>
<p>This member is meant for use by printer interface DLLs, when creating a <b>Document Properties</b> property sheet (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548548">DrvDocumentPropertySheets</a>). It is a constant value specifying which, if any, public member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure is associated with this option. The following table lists available constants, the associated DEVMODE structure member, and the required value for <b>pName</b> for each constant.</p>
<table>
<tr>
<th rowspan="2">Constant Value</th>
<th>Public DEVMODE</th>
<th rowspan="2">Required pName Value</th>
</tr>
<tr>
<th>Structure Member</th>
</tr>
<tr>
<td>
<p>DMPUB_COLOR</p>
</td>
<td>
<p><b>dmColor</b></p>
</td>
<td>
<p>IDS_CPSUI_COLOR_APPERANCE</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_COPIES_COLLATE</p>
</td>
<td>
<p><b>dmCopies</b> and <b>dmCollate</b></p>
</td>
<td>
<p>IDS_CPSUI_COPIES</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_DEFSOURCE</p>
</td>
<td>
<p><b>dmDefSource</b></p>
</td>
<td>
<p>IDS_CPSUI_SOURCE</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_DITHERTYPE</p>
</td>
<td>
<p><b>dmDitherType</b></p>
</td>
<td>
<p>IDS_CPSUI_DITHERING</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_DUPLEX</p>
</td>
<td>
<p><b>dmDuplex</b></p>
</td>
<td>
<p>IDS_CPSUI_DUPLEX</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_FORMNAME</p>
</td>
<td>
<p><b>dmFormName</b></p>
</td>
<td>
<p>IDS_CPSUI_FORMNAME</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_ICMINTENT</p>
</td>
<td>
<p><b>dmICMIntent</b></p>
</td>
<td>
<p>IDS_CPSUI_ICMINTENT</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_ICMMETHOD</p>
</td>
<td>
<p><b>dmICMMethod</b></p>
</td>
<td>
<p>IDS_CPSUI_ICMMETHOD</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_MEDIATYPE</p>
</td>
<td>
<p><b>dmMediaType</b></p>
</td>
<td>
<p>IDS_CPSUI_MEDIA</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_NUP</p>
</td>
<td>
<p>Not contained in public section of DEVMODE.</p>
</td>
<td>
<p>IDS_CPSUI_NUP</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_ORIENTATION</p>
</td>
<td>
<p><b>dmOrientation</b></p>
</td>
<td>
<p>IDS_CPSUI_ORIENTATION</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_OUTPUTBIN</p>
</td>
<td>
<p>Not contained in public section of DEVMODE.</p>
</td>
<td>
<p>IDS_CPSUI_OUTPUTBIN</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_PAGEORDER</p>
</td>
<td>
<p>Not contained in public section of DEVMODE.</p>
</td>
<td>
<p>IDS_CPSUI_PAGEORDER</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_PRINTQUALITY</p>
</td>
<td>
<p><b>dmPrintQuality</b></p>
</td>
<td>
<p>IDS_CPSUI_PRINTQUALITY or IDS_CPSUI_RESOLUTION.</p>
<p>If not specified, the default name is IDS_CPSUI_RESOLUTION.</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_QUALITY</p>
</td>
<td>
<p>Not contained in public section of DEVMODE.</p>
</td>
<td>
<p>IDS_CPSUI_QUALITY_SETTINGS</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_SCALE</p>
</td>
<td>
<p><b>dmScale</b></p>
</td>
<td>
<p>IDS_CPSUI_SCALE</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_TTOPTION</p>
</td>
<td>
<p><b>dmTTOption</b></p>
</td>
<td>
<p>IDS_CPSUI_TTOPTION</p>
</td>
</tr>
<tr>
<td>
<p>DMPUB_NONE</p>
</td>
<td>
<p>Not contained in public section of DEVMODE.</p>
</td>
<td></td>
</tr>
<tr>
<td>
<p>Greater than or equal to DMPUB_USER</p>
</td>
<td>
<p>Ignored by CPSUI, can be a caller-defined value.</p>
</td>
<td></td>
</tr>
</table>
<p> </p>
<p>CPSUI does not maintain a DEVMODE structure. The application is responsible for copying user-selected option parameters into a DEVMODE structure. CPSUI uses <b>DMPubID</b> contents to determine treeview placement of standard options, and to determine the contents of the <b>Layout</b> and <b>Paper/Quality</b> tabs (see the <b>pDlgPage</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure).</p>
<p>For additional information about using the <b>DMPubID</b> member, see the following Remarks section.</p>
</dd>

### -field <b>UserItemID</b>

<dd>
<p>Optional application-supplied value that can be used for option identification purposes. Not referenced by CPSUI.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>

### -field <b>pOIExt</b>

<dd>
<p>Pointer to an optional <a href="https://msdn.microsoft.com/library/windows/hardware/ff559590">OIEXT</a> structure. The caller is responsible for allocating storage for this structure.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved, must be initialized to zero.</p>
</dd>
</dl>

## -remarks
<p>OPTITEM structures should be placed in an array, and the array's address should be placed in the <b>pOptItem</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546211">COMPROPSHEETUI</a> structure.</p>

<p>The <b>Level</b> member allows you to create child nodes in the treeview. For example, to create a set of option nodes under a level 1 parent node, specify level 2 for each child node and include their OPTITEM structures in the OPTITEM array, immediately after the parent's OPTITEM structure. In the parent's OPTITEM structure, <b>pOptType</b> should be <b>NULL</b>. </p>

<p>The treeview root node is level 0. Options displayed when a user expands the root node are level 1. The maximum number of levels is 256.</p>

<p>For option values that are stored in a printer's DEVMODE structure, the <b>DMPubID</b> member must identify the option. For each <b>DMPubID</b> value that is used, a printer interface DLL must specify the <a href="https://msdn.microsoft.com/3b3c002c-a201-4f81-b208-30864343409b">CPSUI option type</a> listed in the following table.</p>

<p>DMPUB_COLOR</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a>
</p>

<p>DMPUB_COPIES_COLLATE</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562853">TVOT_UDARROW</a> plus <a href="https://msdn.microsoft.com/library/windows/hardware/ff548781">EXTCHKBOX</a> (See comments following this table.)</p>

<p>DMPUB_DEFSOURCE</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_DITHERTYPE</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_DUPLEX</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_FORMNAME</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_ICMINTENT</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_ICMMETHOD</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_MEDIATYPE</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_NUP</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_ORIENTATION</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_OUTPUTBIN</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_PAGEORDER</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_PRINTQUALITY</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p>DMPUB_QUALITY</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562825">TVOT_2STATES</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562827">TVOT_3STATES</a>
</p>

<p>DMPUB_SCALE</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562853">TVOT_UDARROW</a>
</p>

<p>DMPUB_TTOPTION</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562839">TVOT_LISTBOX</a>
</p>

<p> </p>

<p>If <b>DMPubID</b> is DMPUB_COPIES_COLLATE and the printer can collate copies, an extended check box (EXTCHKBOX structure) must be provided. The EXTCHCKBOX structure's members must be set as follows:</p>

<p>If OPTIF_EXT_HIDE is not set in <b>Flags</b>, CPSUI enables the check box if a user requests more than one copy, and disables it if only one copy is requested.</p>

<p>Additionally, CPSUI sets the option's display text to <b>copy</b> for one copy and <b>copies</b> for more than one copy.</p>

<p>If <b>DMPubID</b> is DMPUB_COLOR, its first <a href="https://msdn.microsoft.com/library/windows/hardware/ff559660">OPTPARAM</a> structure (<b>Sel</b>=0) must represent Gray Scale, and <b>pData</b> in the OPTPARAM structure must be IDS_CPSUI_GRAYSCALE. Its second OPTPARAM structure (<b>Sel</b>=1) must represent Color, and <b>pData</b> in the OPTPARAM structure must be IDS_CPSUI_COLOR. If another option's <b>DMPubID</b> is DMPUB_ICMINTENT and if Color is not selected, CPSUI disables the option for which DMPUB_ICMINTENT is specified.</p>

<p>CPSUI disables color matching when Color is not selected.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
</table>