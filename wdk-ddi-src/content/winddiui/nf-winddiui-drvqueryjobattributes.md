---
UID: NF.winddiui.DrvQueryJobAttributes
title: DrvQueryJobAttributes
author: windows-driver-content
description: The DrvQueryJobAttributes function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page (&#0034;N-up&#0034; printing), printing multiple copies of each page, collating pages, and printing pages in reverse order.
old-location: print\drvqueryjobattributes.htm
old-project: print
ms.assetid: 71e07572-bb15-4838-94d1-e07a3305ab82
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DrvQueryJobAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrvQueryJobAttributes
req.alt-loc: winddiui.h
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
req.product: Windows 10 or later.
---

# DrvQueryJobAttributes function



## -description
<p>The <b>DrvQueryJobAttributes</b> function allows a printer interface DLL to specify support for such capabilities as printing multiple document pages on a physical page ("N-up" printing), printing multiple copies of each page, collating pages, and printing pages in reverse order.</p>


## -syntax

````
BOOL DrvQueryJobAttributes(
  _In_  HANDLE   hPrinter,
  _In_  PDEVMODE pDevMode,
  _In_  DWORD    dwLevel,
  _Out_ LPBYTE   lpAttributeInfo
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>Caller-supplied printer handle.</p>
</dd>

### -param <i>pDevMode</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</dd>

### -param <i>dwLevel</i> [in]

<dd>
<p>Caller-supplied value indicating the type of structure pointed to by <i>lpAttributeInfo</i>, as indicated in the following table.</p>
<table>
<tr>
<th><i>dwLevel</i> Value</th>
<th>Structure pointed to by <i>lpAttributeInfo</i></th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>
</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545091">ATTRIBUTE_INFO_2</a>
</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>
</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545096">ATTRIBUTE_INFO_4</a>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>lpAttributeInfo</i> [out]

<dd>
<p>Caller-supplied pointer to a structure identified by <i>dwLevel</i>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. Otherwise, it should return <b>FALSE</b>. Returning <b>FALSE</b> causes the current print job to be canceled.</p>

## -remarks
<p>A <a href="NULL">printer interface DLL</a> can optionally provide a <b>DrvQueryJobAttributes</b> function. If the function is provided, it should fill in the supplied structure, described by <i>dwLevel</i> and <i>plAttributeInfo</i>, to indicate the current print job's user-requested attributes (such as N-up parameters and the number of copies) and the driver's ability to support those attributes. The function is typically called by the EMF print processor, so it can determine which job attributes can be handled by the driver (or printer), and which must be handled by the print processor.</p>

<p>For descriptions of the job attributes that the function can specify, see the descriptions of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545091">ATTRIBUTE_INFO_2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545096">ATTRIBUTE_INFO_4</a>.</p>

<p>The ATTRIBUTE_INFO_4 structure is defined for Windows Vista.</p>

<p>A <a href="NULL">printer interface DLL</a> can optionally provide a <b>DrvQueryJobAttributes</b> function. If the function is provided, it should fill in the supplied structure, described by <i>dwLevel</i> and <i>plAttributeInfo</i>, to indicate the current print job's user-requested attributes (such as N-up parameters and the number of copies) and the driver's ability to support those attributes. The function is typically called by the EMF print processor, so it can determine which job attributes can be handled by the driver (or printer), and which must be handled by the print processor.</p>

<p>For descriptions of the job attributes that the function can specify, see the descriptions of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545091">ATTRIBUTE_INFO_2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545096">ATTRIBUTE_INFO_4</a>.</p>

<p>The ATTRIBUTE_INFO_4 structure is defined for Windows Vista.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545090">ATTRIBUTE_INFO_1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545091">ATTRIBUTE_INFO_2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545093">ATTRIBUTE_INFO_3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545096">ATTRIBUTE_INFO_4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20DrvQueryJobAttributes function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
