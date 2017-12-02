---
UID: NS.compstui._INSERTPSUIPAGE_INFO
title: INSERTPSUIPAGE_INFO
author: windows-driver-content
description: The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC_INSERT_PSUIPAGE. All member values must be supplied by the ComPropSheet caller.
old-location: print\insertpsuipage_info.htm
old-project: print
ms.assetid: 99ec8cfa-3ec7-4080-b22a-dba0a86b7e4a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: INSERTPSUIPAGE_INFO, INSERTPSUIPAGE_INFO, *PINSERTPSUIPAGE_INFO
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
req.alt-api: INSERTPSUIPAGE_INFO
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

# INSERTPSUIPAGE_INFO structure



## -description
<p>The INSERTPSUIPAGE_INFO structure is used as an input parameter to CPSUI's <a href="print.compropsheet">ComPropSheet</a> function, if the function code is <a href="print.cpsfunc_insert_psuipage">CPSFUNC_INSERT_PSUIPAGE</a>. All member values must be supplied by the <b>ComPropSheet</b> caller.</p>


## -syntax

````
typedef struct _INSERTPSUIPAGE_INFO {
  WORD      cbSize;
  BYTE      Type;
  BYTE      Mode;
  ULONG_PTR dwData1;
  ULONG_PTR dwData2;
  ULONG_PTR dwData3;
} INSERTPSUIPAGE_INFO, *PINSERTPSUIPAGE_INFO;
````


## -struct-fields
<dl>

### -field cbSize

<dd>
<p>Caller-supplied size, in bytes, of the INSERTPSUIPAGE_INFO structure.</p>
</dd>

### -field Type

<dd>
<p>Caller-supplied integer value indicating the type of insertion being requested. The member can contain one of the following constants:</p>
<p></p>
<dl>

### -field PSUIPAGEINSERT_DLL

<dd>
<p>CPSUI calls the specified <a href="..\compstui\nc-compstui-pfnpropsheetui.md">PFNPROPSHEETUI</a> typed function, with a reason value of PROPSHEETUI_REASON_INIT. The function is contained in a separate DLL.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_GROUP_PARENT

<dd>
<p>CPSUI creates a new <a href="https://msdn.microsoft.com/b4c40c15-df16-4af0-81c8-9e70d26ba598">group parent</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_HPROPSHEETPAGE

<dd>
<p>CPSUI inserts a page that has been created by calling <b>CreatePropertySheetPage</b> (see the Microsoft Windows SDK documentation).</p>
<p>(This is equivalent to calling <a href="print.compropsheet">ComPropSheet</a> with a function code of <a href="print.cpsfunc_add_hpropsheetpage">CPSFUNC_ADD_HPROPSHEETPAGE</a>.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PCOMPROPSHEETUI

<dd>
<p>CPSUI inserts pages described by a <a href="..\compstui\ns-compstui--compropsheetui.md">COMPROPSHEETUI</a> structure.</p>
<p>(This is equivalent to calling <a href="print.compropsheet">ComPropSheet</a> with a function code of <a href="print.cpsfunc_add_pcompropsheetui">CPSFUNC_ADD_PCOMPROPSHEETUI</a>.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PFNPROPSHEETUI

<dd>
<p>CPSUI calls the specified <a href="..\compstui\nc-compstui-pfnpropsheetui.md">PFNPROPSHEETUI</a> typed function, with a reason value of PROPSHEETUI_REASON_INIT.</p>
<p>(This is equivalent to calling <a href="print.compropsheet">ComPropSheet</a> with a function code of <a href="print.cpsfunc_add_pfnpropsheetui">CPSFUNC_ADD_PFNPROPSHEETUI</a>.)</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PROPSHEETPAGE

<dd>
<p>CPSUI inserts the page described by the specified PROPSHEETPAGE structure.</p>
<p>(This is equivalent to calling <a href="print.compropsheet">ComPropSheet</a> with a function code of <a href="print.cpsfunc_add_propsheetpage">CPSFUNC_ADD_PROPSHEETPAGE</a>.)</p>
</dd>
</dl>
</dd>

### -field Mode

<dd>
<p>Caller-supplied value indicating where CPSUI should insert the new pages. It must be one of the following values:</p>
<p></p>
<dl>

### -field INSPSUIPAGE_MODE_AFTER

<dd>
<p>CPSUI inserts pages after the page identified by the CPSUI page handle that is specified by the <i>lParam1</i> parameter to <a href="print.compropsheet">ComPropSheet</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field INSPSUIPAGE_MODE_BEFORE

<dd>
<p>CPSUI inserts pages before the page identified by the CPSUI page handle that is specified by the <i>lParam1</i> parameter to <a href="print.compropsheet">ComPropSheet</a>.</p>
</dd>
</dl>
<p></p>
<dl>

### -field INSPSUIPAGE_MODE_FIRST_CHILD

<dd>
<p>CPSUI inserts pages as the first children of the parent group identified by the <i>hComPropSheet</i> parameter to <a href="print.compropsheet">ComPropSheet</a>.</p>
<p>The <i>lParam1</i> parameter to <a href="print.compropsheet">ComPropSheet</a> is ignored.</p>
</dd>
</dl>
<p></p>
<dl>

### -field INSPUIPAGE_MODE_INDEX

<dd>
<p>CPSUI inserts pages as children of the parent group identified by the <i>hComPropSheet</i> parameter to <a href="print.compropsheet">ComPropSheet</a>.</p>
<p>The <i>lParam1</i> parameter to <a href="print.compropsheet">ComPropSheet</a> specifies a zero-based index identifying where, within the set of children, the specified pages should be inserted. If <i>lParam1</i> is 0, the pages are inserted starting at page 1; if <i>lParam1</i> is 1, the pages are inserted starting at page 2; and so on. If the index is greater than the number of existing children, the new pages are added as the last children. The <i>lParam1</i> value must be specified as HINSPSUIPAGE_INDEX(index).</p>
</dd>
</dl>
<p></p>
<dl>

### -field INSPSUIPAGE_MODE_LAST_CHILD

<dd>
<p>CPSUI inserts pages as the last children of the parent group identified by the <i>hComPropSheet</i> parameter to <a href="print.compropsheet">ComPropSheet</a>.</p>
<p>The <i>lParam1</i> parameter to <a href="print.compropsheet">ComPropSheet</a> is ignored.</p>
</dd>
</dl>
</dd>

### -field dwData1

<dd></dd>

### -field dwData2

<dd></dd>

### -field dwData3

<dd>
<p>Caller-supplied values that depend on the contents of the <b>Type</b> member, as follows:</p>
<p></p>
<dl>

### -field PSUIPAGEINSERT_DLL

<dd>
<p>dwData1 - Caller-supplied pointer to a NULL-terminated string representing the DLL path name.</p>
<p>dwData2 - Caller-supplied pointer to a NULL-terminated string representing the name of a <a href="..\compstui\nc-compstui-pfnpropsheetui.md">PFNPROPSHEETUI</a> typed function, contained in the specified DLL.</p>
<p>dwData3 - Caller-supplied 32-bit value, passed to the PFNPROPSHEETUI-typed function for its <i>lParam</i> parameter.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_GROUP_PARENT

<dd>
<p>dwData1 - Not used, must be zero.</p>
<p>dwData2 - Not used, must be zero.</p>
<p>dwData3 - Not used, must be zero.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_HPROPSHEETPAGE

<dd>
<p>dwData1 - Caller-supplied handle to a property sheet, returned by <b>CreatePropertySheetPage</b>.</p>
<p>dwData2 - Not used, must be zero.</p>
<p>dwData3 - Not used, must be zero.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PCOMPROPSHEETUI

<dd>
<p>dwData1 - Caller-supplied pointer to a COMPROPSHEETUI structure.</p>
<p>dwData2 - On success, receives the number of pages inserted. On failure, receives an ERR_CPSUI-prefixed error code.</p>
<p>dwData3 - Not used, must be zero.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PFNPROPSHEETUI

<dd>
<p>dwData1 - Caller-supplied pointer to a PFNPROPSHEETUI-typed function.</p>
<p>dwData2 - Caller-supplied 32-bit value, passed to the PFNPROPSHEETUI-typed function for its <i>lParam</i> parameter.</p>
<p>dwData3 - Not used, must be zero.</p>
</dd>
</dl>
<p></p>
<dl>

### -field PSUIPAGEINSERT_PROPSHEETPAGE

<dd>
<p>dwData1 - Caller-supplied pointer to a PROPSHEETPAGE structure.</p>
<p>dwData2 - Not used, must be zero.</p>
<p>dwData3 - Not used, must be zero.</p>
</dd>
</dl>
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