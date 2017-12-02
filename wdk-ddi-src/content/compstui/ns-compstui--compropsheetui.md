---
UID: NS.compstui._COMPROPSHEETUI
title: COMPROPSHEETUI
author: windows-driver-content
description: The COMPROPSHEETUI structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_ADD_PCOMPROPSHEETUI. All structure members must be supplied by the caller of ComPropSheet.
old-location: print\compropsheetui.htm
old-project: print
ms.assetid: 7ebf46b7-5c31-482e-8644-a3d81f7dc5cc
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: COMPROPSHEETUI, COMPROPSHEETUI, *PCOMPROPSHEETUI
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
req.alt-api: COMPROPSHEETUI
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

# COMPROPSHEETUI structure



## -description
<p>The COMPROPSHEETUI structure is used as an input parameter to CPSUI's <a href="print.compropsheet">ComPropSheet</a> function, if the function code is <a href="print.cpsfunc_add_pcompropsheetui">CPSFUNC_ADD_PCOMPROPSHEETUI</a>. All structure members must be supplied by the caller of <i>ComPropSheet</i>.</p>


## -syntax

````
typedef struct _COMPROPSHEETUI {
  WORD           cbSize;
  WORD           Flags;
  HINSTANCE      hInstCaller;
  LPTSTR         pCallerName;
  ULONG_PTR      UserData;
  LPTSTR         pHelpFile;
  _CPSUICALLBACK pfnCallBack;
  POPTITEM       pOptItem;
  PDLGPAGE       pDlgPage;
  WORD           cOptItem;
  WORD           cDlgPage;
  ULONG_PTR      IconID;
  LPTSTR         pOptItemName;
  WORD           CallerVersion;
  WORD           OptItemVersion;
  ULONG_PTR      dwReserved[4];
} COMPROPSHEETUI, *PCOMPROPSHEETUI;
````


## -struct-fields
<dl>

### -field cbSize

<dd>
<p>Caller-supplied size, in bytes, of the COMPROPSHEETUI structure.</p>
</dd>

### -field Flags

<dd>
<p>Optional caller-supplied bit flags, as described in the following list:</p>
<p></p>
<dl>

### -field CPSUIF_ABOUT_CALLBACK

<dd>
<p>If set, the page's callback function (pointed to by the structure's <b>pfnCallback</b> member), supports CPSUICB_REASON_ABOUT, so CPSUI will call the callback function if the user clicks on the page's <b>About</b> button. (CPSUI supplies an <b>About</b> button for each treeview root node.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field CPSUIF_ICONID_AS_HICON

<dd>
<p>If set, the structure's <b>IconID</b> member contains an icon handle.</p>
<p>If not set, the <b>IconID</b> member contains an icon resource identifier.</p>
</dd>
</dl>
<p></p>
<dl>

### -field CPSUIF_UPDATE_PERMISSION

<dd>
<p>If set, the page's option values can be modified by the user.</p>
</dd>
</dl>
</dd>

### -field hInstCaller

<dd>
<p>Caller-supplied module instance handle, received by the DLL's entry point function.</p>
</dd>

### -field pCallerName

<dd>
<p>Caller-supplied pointer to a NULL-terminated text string representing the application's name. (For a printer interface DLL, this should be the driver's name, such as "PostScript Driver".)</p>
</dd>

### -field UserData

<dd>
<p>Optional caller-supplied value, which CPSUI places in a <a href="..\compstui\ns-compstui--cpsuicbparam.md">CPSUICBPARAM</a> structure's <b>UserData</b> member when calling the function pointed to by <b>pfnCallBack</b>.</p>
</dd>

### -field pHelpFile

<dd>
<p>Caller-supplied pointer to a NULL-terminated text string representing a path to a help file. For printer interface DLLs, this is typically the help file path obtained by calling GetPrinterDriver (described in the Microsoft Windows SDK documentation).</p>
<p>The help file is indexed by values contained in the <b>HelpIndex</b> member of <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> structures.</p>
</dd>

### -field pfnCallBack

<dd>
<p>Caller-supplied pointer to a <a href="..\compstui\nc-compstui--cpsuicallback.md">_CPSUICALLBACK</a>-typed callback function, which CPSUI calls when a user modifies the page's option values.</p>
<p>Can be used only if <b>pDlgPage</b> identifies a CPSUI-supplied <a href="..\compstui\ns-compstui--dlgpage.md">DLGPAGE</a> structure, or if the <b>DlgProc</b> member of an application-supplied DLGPAGE structure is <b>NULL</b>.</p>
</dd>

### -field pOptItem

<dd>
<p>Caller-supplied pointer to an array of <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> structures describing the page's options.</p>
</dd>

### -field pDlgPage

<dd>
<p>This member specifies <a href="..\compstui\ns-compstui--dlgpage.md">DLGPAGE</a> structures that describe pages to be added to the property sheet. It can be either of the following:</p>
<ul>
<li>
<p>A pointer to an array of DLGPAGE structures.</p>
</li>
<li>
<p>One of the pointers that is described in the following list. These pointers reference predefined DLGPAGE structures, supplied by CPSUI for use by printer interface DLLs.<p></p>
<dl>

### -field CPSUI_PDLGPAGE_ADVDOCPROP

<dd>
<p>Defines one treeview page whose tab reads <b>Advanced</b>.</p>
<p>For use only by a <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a> function.</p>
</dd>
</dl>
<p></p>
<dl>

### -field CPSUI_PDLGPAGE_DOCPROP

<dd>
<p>Defines three pages, whose tabs are <b>Layout</b>, <b>Paper/Quality</b>, and <b>Advanced</b>. The <b>Advanced</b> page is a treeview.</p>
<p>For use only by a <a href="..\winddiui\nf-winddiui-drvdocumentpropertysheets.md">DrvDocumentPropertySheets</a> function.</p>
</dd>
</dl>
<p></p>
<dl>

### -field CPSUI_PDLGPAGE_PRINTERPROP

<dd>
<p>Defines one treeview page whose tab reads <b>Device Settings</b>.</p>
<p>For use only by a <a href="..\winddiui\nf-winddiui-drvdevicepropertysheets.md">DrvDevicePropertySheets</a> function.</p>
</dd>
</dl>
<p></p>
<dl>

### -field CPSUI_PDLGPAGE_TREEVIEWONLY

<dd>
<p>Defines one treeview page.</p>
</dd>
</dl>
</p>
</li>
</ul>
</dd>

### -field cOptItem

<dd>
<p>Caller-supplied number of <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> structures pointed to by <b>pOptItem</b>.</p>
</dd>

### -field cDlgPage

<dd>
<p>Caller-supplied number of <a href="..\compstui\ns-compstui--dlgpage.md">DLGPAGE</a> structures pointed to by <b>pDlgPage</b>. Not used if <b>pDlgPage</b> specifies a predefined CPSUI_PDLGPAGE-prefixed structure.</p>
</dd>

### -field IconID

<dd>
<p>Caller-supplied, can be one of the following:</p>
<ul>
<li>
<p>An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI_CPSUI-prefixed icon resource identifiers.</p>
</li>
<li>
<p>An icon handle. If a handle is specified, CPSUIF_ICONID_AS_HICON must be set in the <b>Flags</b> member.</p>
</li>
</ul>
<p>The specified icon is displayed in the root node of the property sheet page's treeview.</p>
</dd>

### -field pOptItemName

<dd>
<p>Caller-supplied pointer to a NULL-terminated string to be displayed in the root node of the property sheet page's treeview. For printer interface DLLs, this string typically represents a printer device type, such as "HP 4si".</p>
</dd>

### -field CallerVersion

<dd>
<p>Caller-supplied version number, representing the calling application's current version. The high byte identifies the major version, and the low byte is the minor version. For example, a <b>CallerVersion</b> value of 0x310 specifies a caller version number of 3.16. The version number is displayed when a user clicks on a page's <b>About</b> button.</p>
</dd>

### -field OptItemVersion

<dd>
<p>Caller-supplied version number, representing the root-level option item's current version. For printer interface DLLs, this typically represents a printer device version. The high byte identifies the major version, and the low byte is the minor version. For example, an <b>OptItemVersion</b> value of 0x3ff specifies a caller version number of 3.255. The version number is displayed when a user clicks on a page's <b>About</b> button.</p>
</dd>

### -field dwReserved

<dd>
<p>Reserved. This array must be set to zero.</p>
</dd>
</dl>

## -remarks


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