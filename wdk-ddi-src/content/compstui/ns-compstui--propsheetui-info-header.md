---
UID: NS.compstui._PROPSHEETUI_INFO_HEADER
title: PROPSHEETUI_INFO_HEADER
author: windows-driver-content
description: The PROPSHEETUI_INFO_HEADER structure is used as an input parameter to an application's PFNPROPSHEETUI-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_INFO_HEADER.
old-location: print\propsheetui_info_header.htm
old-project: print
ms.assetid: 148c463c-a18b-4f24-b3dc-af74c3de97b7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PROPSHEETUI_INFO_HEADER, PROPSHEETUI_INFO_HEADER, *PPROPSHEETUI_INFO_HEADER
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
req.alt-api: PROPSHEETUI_INFO_HEADER
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

# PROPSHEETUI_INFO_HEADER structure



## -description
<p>The PROPSHEETUI_INFO_HEADER structure is used as an input parameter to an application's <a href="..\compstui\nc-compstui-pfnpropsheetui.md">PFNPROPSHEETUI</a>-typed function, when the function is called with a reason value of PROPSHEETUI_REASON_GET_INFO_HEADER.</p>


## -syntax

````
typedef struct _PROPSHEETUI_INFO_HEADER {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  HWND      hWndParent;
  HINSTANCE hInst;
  union {
    HICON     hIcon;
    ULONG_PTR IconID;
  };
} PROPSHEETUI_INFO_HEADER, *PPROPSHEETUI_INFO_HEADER;
````


## -struct-fields
<dl>

### -field cbSize

<dd>
<p>CPSUI-supplied size, in bytes, of the PROPSHEETUI_INFO_HEADER structure.</p>
</dd>

### -field Flags

<dd>
<p>Optional, application-specified bit flags that modify the property sheet page's appearance. The flags listed in the following table can be used in any combination.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>PSUIHDRF_DEFTITLE</p>
</td>
<td>
<p>If set, CPSUI should include "Default" in the title bar string. CPSUI adds "Default" after the <b>pTitle</b> string and, if PSUIHDRF_PROPTITLE is set, before "Properties".</p>
</td>
</tr>
<tr>
<td>
<p>PSUIHDRF_EXACT_PTITLE</p>
</td>
<td>
<p>If set, CPSUI uses the text specified by <b>pTitle</b> without modification. This flag overrides PSUIHDRF_DEFTITLE and PSUIHDRF_PROPTITLE.</p>
</td>
</tr>
<tr>
<td>
<p>PSUIHDRF_NOAPPLYNOW</p>
</td>
<td>
<p>If set, CPSUI should not include an <b>Apply Now</b> button.</p>
</td>
</tr>
<tr>
<td>
<p>PSUIHDRF_PROPTITLE</p>
</td>
<td>
<p>If set, CPSUI should append "Properties" to the title bar string. (By default, CPSUI sets this flag before calling the application.)</p>
</td>
</tr>
<tr>
<td>
<p>PSUIHDRF_USEHICON</p>
</td>
<td>
<p>If set, the <b>hIcon</b>/<b>IconID</b> union contains an icon handle. If not set, the union contains an icon resource identifier.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field pTitle

<dd>
<p>String identifier, representing text to be displayed in the property sheet's title bar. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero. For printer interface DLLs, the string typically contains the printer's name.</p>
</dd>

### -field hWndParent

<dd>
<p>Handle to the window to be used as the parent of the property sheet. By default, CPSUI supplies the window handle that it received for the <i>hWndOwner</i> parameter to <a href="print.commonpropertysheetui">CommonPropertySheetUI</a>, but the application can overwrite that handle with another.</p>
</dd>

### -field hInst

<dd>
<p>Application-supplied instance handle, which CPSUI uses when loading application resources.</p>
</dd>

### -field hIcon

<dd></dd>

### -field IconID

<dd>
<p>This union identifies the icon to be displayed in the property sheet's title bar. The union member is selected by PSUIHDRF_USEICON in <b>Flags</b>.</p>
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