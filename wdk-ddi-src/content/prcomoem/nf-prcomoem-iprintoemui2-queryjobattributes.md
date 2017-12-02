---
UID: NF.prcomoem.IPrintOemUI2.QueryJobAttributes
title: IPrintOemUI2::QueryJobAttributes
author: windows-driver-content
description: The IPrintOemUI2::QueryJobAttributes method allows a UI plug-in to postprocess the core driver's results after a call to the DrvQueryJobAttributes DDI.
old-location: print\iprintoemui2_queryjobattributes.htm
old-project: print
ms.assetid: cb510aa6-7156-4b02-bab1-6951becbc1a0
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI2, QueryJobAttributes, IPrintOemUI2::QueryJobAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUI2.QueryJobAttributes
req.alt-loc: prcomoem.h
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
req.iface: IPrintOemUI2
req.product: Windows 10 or later.
---

# IPrintOemUI2::QueryJobAttributes method



## -description
<p>The <code>IPrintOemUI2::QueryJobAttributes</code> method allows a UI plug-in to postprocess the core driver's results after a call to the <a href="..\winddiui\nf-winddiui-drvqueryjobattributes.md">DrvQueryJobAttributes</a> DDI. The plug-in can choose to overwrite the values that the core driver placed in the <i>lpAttributeInfo</i> output buffer.</p>


## -syntax

````
HRESULT QueryJobAttributes(
   HANDLE   hPrinter,
   PDEVMODE pDevmode,
   DWORD    dwLevel,
   LPBYTE   lpAttributeInfo
);
````


## -parameters
<dl>

### -param hPrinter 

<dd>
<p>Specifies the caller-supplied printer handle.</p>
</dd>

### -param pDevmode 

<dd>
<p>Pointer to a caller-supplied <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>

### -param dwLevel 

<dd>
<p>Specifies a caller-supplied value indicating the type of structure pointed to by <i>lpAttributeInfo</i>, as indicated in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Structure Pointed to by <i>lpAttributeInfo</i></th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>
<a href="..\winddiui\ns-winddiui--attribute-info-1.md">ATTRIBUTE_INFO_1</a>
</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>
<a href="..\winddiui\ns-winddiui--attribute-info-2.md">ATTRIBUTE_INFO_2</a>
</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>
<a href="..\winddiui\ns-winddiui--attribute-info-3.md">ATTRIBUTE_INFO_3</a>
</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>
<a href="..\winddiui\ns-winddiui--attribute-info-4.md">ATTRIBUTE_INFO_4</a>
</p>
</td>
</tr>
</table>
<p> </p>
<dl>
<dd>
<p>Note that if this method changes any dwDrv<i>Xxx</i> member of the ATTRIBUTE_INFO_<i>N</i> structures, the spooler assumes that the plug-in is able to support the behavior represented by that member.</p>
</dd>
</dl>
</dd>

### -param lpAttributeInfo 

<dd>
<p>Pointer to a memory location that receives the address of a structure of the type identified by <i>dwLevel</i>.</p>
</dd>
</dl>

## -returns
<p>If the UI plug-in supports this method, and the method succeeded, it should return S_OK. This causes the core driver to return <b>TRUE</b> for the <a href="..\winddiui\nf-winddiui-drvqueryjobattributes.md">DrvQueryJobAttributes</a> DDI. If the UI plug-in supports this method, but the method failed, it should return E_FAIL. This causes the core driver to return <b>FALSE</b> for the DrvQueryJobAttributes DDI. If the UI plug-in does not support this method, it should return E_NOTIMPL.</p>

## -remarks
<p>When the printer has multiple UI plug-ins installed, the core driver calls the UI plug-ins in the order they were installed. The HRESULT returned by the last UI plug-in that supports this method is used to determine the core driver's DrvQueryJobAttributes DDI return value as described in the previous section.</p>

<p>See <a href="..\winddiui\nf-winddiui-drvqueryjobattributes.md">DrvQueryJobAttributes</a> for more information.</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winddiui\ns-winddiui--attribute-info-1.md">ATTRIBUTE_INFO_1</a>
</dt>
<dt>
<a href="..\winddiui\ns-winddiui--attribute-info-2.md">ATTRIBUTE_INFO_2</a>
</dt>
<dt>
<a href="..\winddiui\ns-winddiui--attribute-info-3.md">ATTRIBUTE_INFO_3</a>
</dt>
<dt>
<a href="..\winddiui\ns-winddiui--attribute-info-4.md">ATTRIBUTE_INFO_4</a>
</dt>
<dt>
<a href="display.devmodew">DEVMODEW</a>
</dt>
<dt>
<a href="..\winddiui\nf-winddiui-drvqueryjobattributes.md">DrvQueryJobAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI2::QueryJobAttributes method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
