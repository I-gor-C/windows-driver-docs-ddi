---
UID: NS.compstui._SETRESULT_INFO
title: SETRESULT_INFO
author: windows-driver-content
description: The SETRESULT_INFO structure is used as an input parameter to an application's PFNPROPSHEETUI-typed callback function.
old-location: print\setresult_info.htm
ms.assetid: 54701f88-1145-4a50-bf5a-36be1d88355d
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SETRESULT_INFO
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# SETRESULT_INFO structure



## -description
<p>The SETRESULT_INFO structure is used as an input parameter to an application's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559812">PFNPROPSHEETUI</a>-typed callback function. </p>


## -syntax

````
typedef struct _SETRESULT_INFO {
  WORD    cbSize;
  WORD    wReserved;
  HANDLE  hSetResult;
  LRESULT Result;
} SETRESULT_INFO, *PSETRESULT_INFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd>
<p>CPSUI-supplied size, in bytes, of the SETRESULT_INFO structure.</p>
</dd>

### -field <b>wReserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>hSetResult</b>

<dd>
<p>CPSUI-supplied handle to an added property sheet page, obtained from the application. For more information, see the following Remarks section.</p>
</dd>

### -field <b>Result</b>

<dd>
<p>CPSUI-supplied handle to an added property sheet page, obtained from the application. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -remarks
<p>When an application calls CPSUI's <a href="https://msdn.microsoft.com/library/windows/hardware/ff546207">ComPropSheet</a> function, specifying a function code of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547087">CPSFUNC_SET_RESULT</a>, CPSUI calls all registered <a href="https://msdn.microsoft.com/library/windows/hardware/ff559812">PFNPROPSHEETUI</a>-typed functions, specifying a reason of PROPSHEETUI_REASON_SET_RESULT. When specifying this reason, CPSUI also supplies a SETRESULT_INFO structure.</p>

<p>The values contained in the structure's <b>hSetResult</b> and <b>Result</b> members are the <i>lParam1</i> and <i>lParam2</i> values, respectively, that were supplied to CPSUI's <b>ComPropSheet</b> function.</p>

<p>Each of the application's PFNPROPSHEETUI-typed functions is called in order, from the one most recently declared to the first one declared, until one of these functions provides a return value of less than one. At that point, CPSUI returns from its <b>ComPropSheet</b> function, providing a count of the number of PFNPROPSHEETUI-typed functions that were called.</p>

<p>Typically, an application's PFNPROPSHEETUI-typed function sets the <b>Result</b> member of its PROPSHEETUI_INFO structure to the value received in the SETRESULT_INFO structure's <b>Result</b> member. Then the function returns a value of 1 (or greater), so the next PFNPROPSHEETUI-typed function can also receive it. Each subsequently called function is associated with a page that is the parent of the page associated with the last-called function. A function can modify the contents of SETRESULT_INFO structure's <b>Result</b> member, causing the functions associated with parent pages to receive the new value.</p>

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