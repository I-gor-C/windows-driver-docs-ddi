---
UID: NS.compstui._PSPINFO
title: PSPINFO
author: windows-driver-content
description: The PSPINFO structure is used as an input parameter to a property sheet page's dialog box procedure, when the Windows message is WM_INITDIALOG. The dialog box procedure's address is specified in a DLGPAGE structure.
old-location: print\pspinfo.htm
old-project: print
ms.assetid: 80a15ee4-e160-49fc-9c61-a14b14d19751
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PSPINFO, PSPINFO, *PPSPINFO
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
req.alt-api: PSPINFO
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

# PSPINFO structure



## -description
<p>The PSPINFO structure is used as an input parameter to a property sheet page's dialog box procedure, when the Windows message is WM_INITDIALOG. The dialog box procedure's address is specified in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> structure.</p>


## -syntax

````
typedef struct _PSPINFO {
  WORD            cbSize;
  WORD            wReserved;
  HANDLE          hComPropSheet;
  HANDLE          hCPSUIPage;
  PFNCOMPROPSHEET pfnComPropSheet;
} PSPINFO, *PPSPINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>CPSUI-supplied size, in bytes, of the PSPINFO structure.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>hComPropSheet</b>

<dd>
<p>CPSUI-supplied handle to the parent of the page whose handle is contained in <b>hCPSUIPage</b>.</p>
</dd>

### -field <b>hCPSUIPage</b>

<dd>
<p>CPSUI-supplied handle to the property sheet page.</p>
</dd>

### -field <b>pfnComPropSheet</b>

<dd>
<p>CPSUI-supplied pointer to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff546207">ComPropSheet</a> function.</p>
</dd>
</dl>

## -remarks
<p>Before CPSUI calls <b>CreatePropertySheetPage</b> to create a property sheet page, it expands the size of the standard PROPSHEETPAGE structure in order to append a PSPINFO structure. When the operating system calls a dialog box procedure (pointed to by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> structure) and specifies a WM_INITDIALOG message, the function's <b>lParam</b> member points to the expanded PROPSHEETPAGE structure containing the PSPINFO structure.</p>

<p>(The <b>CreatePropertySheetPage</b> function, PROPSHEETPAGE structure, WM_INITDIALOG message, and dialog box procedures are all described in the Microsoft Windows SDK documentation.)</p>

<p>To obtain the PSPINFO structure's address, use the PPSPINFO_FROM_WM_INITDIALOG_LPARAM macro (defined in compstui.h) as follows:</p>

<p>The PSPINFO structure pointer can be saved for later use, but the structure's contents must not be modified.</p>

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