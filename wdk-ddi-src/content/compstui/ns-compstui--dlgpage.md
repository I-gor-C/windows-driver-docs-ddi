---
UID: NS.compstui._DLGPAGE
title: DLGPAGE
author: windows-driver-content
description: The DLGPAGE structure is used for specifying a property sheet page to CPSUI's ComPropSheet function. The structure's address is included in a COMPROPSHEETUI structure, and all member values are supplied by the ComPropSheet caller.
old-location: print\dlgpage.htm
old-project: print
ms.assetid: 61fb66b9-afd7-4ec4-bbbb-66a287398484
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DLGPAGE, DLGPAGE, *PDLGPAGE
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
req.alt-api: DLGPAGE
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

# DLGPAGE structure



## -description
<p>The DLGPAGE structure is used for specifying a property sheet page to CPSUI's <a href="print.compropsheet">ComPropSheet</a> function. The structure's address is included in a <a href="..\compstui\ns-compstui--compropsheetui.md">COMPROPSHEETUI</a> structure, and all member values are supplied by the <b>ComPropSheet</b> caller.</p>


## -syntax

````
typedef struct _DLGPAGE {
  WORD      cbSize;
  WORD      Flags;
  DLGPROC   DlgProc;
  LPTSTR    pTabName;
  ULONG_PTR IconID;
  union {
    WORD   DlgTemplateID;
    HANDLE hDlgTemplate;
  };
} DLGPAGE, *PDLGPAGE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>Caller-supplied size, in bytes, of the DLGPAGE structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Caller-supplied bit flags, as described in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DPF_ICONID_AS_HICON</p>
</td>
<td>
<p>If set, IconID contains an icon handle.</p>
<p>If not set, IconID contains an icon resource identifier.</p>
</td>
</tr>
<tr>
<td>
<p>DPF_USE_HDLGTEMPLATE</p>
</td>
<td>
<p>If set, <b>hDlgTemplate</b> contains a template handle.</p>
<p>If not set, <b>DlgTemplateID</b> contains a template resource identifier.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DlgProc</b>

<dd>
<p>Optional, caller-supplied DLGPROC-typed pointer to a dialog box procedure, used to process messages sent by the system when user events occur. (The DLGPROC pointer type is described in the Microsoft Windows SDK documentation.) If <b>NULL</b>, CPSUI supplies a dialog box procedure. For more information, see the following Remarks section.</p>
</dd>

### -field <b>pTabName</b>

<dd>
<p>Caller-supplied pointer to a NULL-terminated string to be displayed on the page tab.</p>
</dd>

### -field <b>IconID</b>

<dd>
<p>Caller-supplied, can be one of the following:</p>
<ul>
<li>
<p>An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI_CPSUI-prefixed icon resource identifiers.</p>
</li>
<li>
<p>An icon handle. If a handle is specified, DPF_ICONID_AS_HICON must be set in the <b>Flags</b> member.</p>
</li>
</ul>
<p>The specified icon is displayed on the page tab. If this value is zero, an icon is not displayed.</p>
</dd>

### -field <b>DlgTemplateID</b>

<dd>
<p>Caller-supplied resource identifier for a dialog box template. This can refer to an application-supplied DIALOG resource, or it can be one of the following CPSUI-supplied identifiers (defined in compstui.h):</p>
<table>
<tr>
<th>Identifier</th>
<th>Type of Page</th>
</tr>
<tr>
<td>
<p>DP_STD_DOCPROPPAGE1</p>
</td>
<td>
<p>Nontreeview page, used for a print document's <b>Layout</b> page.</p>
</td>
</tr>
<tr>
<td>
<p>DP_STD_DOCPROPPAGE2</p>
</td>
<td>
<p>Nontreeview page, used for a print document's <b>Paper/Quality</b> page.</p>
</td>
</tr>
<tr>
<td>
<p>DP_STD_TREEVIEWPAGE</p>
</td>
<td>
<p>Generic treeview page.</p>
</td>
</tr>
</table>
<p> </p>
<p>The CPSUI-supplied identifiers refer to templates that can display <a href="https://msdn.microsoft.com/library/windows/hardware/ff547142">CPSUI option types</a>. The page size for those templates is 252 by 216 dialog box units. For more information, see <a href="https://msdn.microsoft.com/de33cb29-3941-4232-bd61-d36fb04d69d3">CPSUI-Supplied Pages and Templates</a>.</p>
<p>This member is not used if DPF_USE_HDLGTEMPLATE is set in <b>Flags</b>.</p>
</dd>

### -field <b>hDlgTemplate</b>

<dd>
<p>Caller-supplied handle to a DLGTEMPLATE structure (described in the Microsoft Windows SDK documentation).</p>
<p>Used only if DPF_USE_HDLGTEMPLATE is set in <b>Flags</b>.</p>
</dd>
</dl>

## -remarks
<p>CPSUI creates a property sheet page by allocating a PROPSHEETPAGE structure and passing it to CreatePropertySheetPage (described in the Windows SDK documentation). If the caller has specified a DLGPROC-typed pointer to a dialog box procedure in <b>DlgProc</b>, that procedure is used for handling the page's window messages. If <b>DlgProc</b> is <b>NULL</b>, CPSUI's own dialog box procedures are used.</p>

<p>When the dialog box procedure pointed to by <b>DlgProc</b> is called with a message value of WM_INITDIALOG, it receives the PROPSHEETPAGE structure as input, and it also receives a <a href="..\compstui\ns-compstui--pspinfo.md">PSPINFO</a> structure.</p>

<p>If a caller-supplied dialog box procedure handles a message, it should return a nonzero value. If the function does not handle the message it should return zero, which causes CPSUI to handle the message.</p>

<p>The PROPSHEETPAGE structure, the DLGPROC pointer type, and the WM_INITDIALOG message are described in the Windows SDK documentation.</p>

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