---
UID: NF.winsplp.GetJobAttributesEx
title: GetJobAttributesEx
author: windows-driver-content
description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
old-location: print\getjobattributesex.htm
old-project: print
ms.assetid: 0715e4d4-665c-42cb-9c74-48c2c558c277
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GetJobAttributesEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: This function is available in the Windows Vista operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetJobAttributesEx
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# GetJobAttributesEx function



## -description

## -syntax

````
BOOL GetJobAttributesEx(
  _In_  LPWSTR     pPrinterName,
  _In_  LPDEVMODEW pDevmode,
  _In_  DWORD      dwLevel,
  _Out_ LPBYTE     pAttributeInfo,
  _In_  DWORD      nSize,
  _In_  DWORD      dwFlags
);
````


## -parameters
<dl>

### -param <i>pPrinterName</i> [in]

<dd>
<p>Caller-supplied pointer to a NULL-terminated Unicode string that contains the printer name.</p>
</dd>

### -param <i>pDevmode</i> [in]

<dd>
<p>Caller-supplied pointer to a <a href="display.devmodew">DEVMODEW</a> structure that is passed to the print processor or printer driver.</p>
</dd>

### -param <i>dwLevel</i> [in]

<dd>
<p>Caller-supplied value that indicates the type of structure pointed to by <i>pAttributeInfo</i>, as indicated in the following table. For more information, see Remarks.</p>
<table>
<tr>
<th><i>dwLevel</i> Value</th>
<th>Structure pointed to by <i>pAttributeInfo</i></th>
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
</dd>

### -param <i>pAttributeInfo</i> [out]

<dd>
<p>Caller-supplied pointer to an attribute information structure (<a href="..\winddiui\ns-winddiui--attribute-info-1.md">ATTRIBUTE_INFO_1</a>, <a href="..\winddiui\ns-winddiui--attribute-info-2.md">ATTRIBUTE_INFO_2</a>, <a href="..\winddiui\ns-winddiui--attribute-info-3.md">ATTRIBUTE_INFO_3</a>, or <a href="..\winddiui\ns-winddiui--attribute-info-4.md">ATTRIBUTE_INFO_4</a>) that receives information about the print job.</p>
</dd>

### -param <i>nSize</i> [in]

<dd>
<p>Size of the buffer, in bytes, pointed to by <i>pAttributeInfo</i>.</p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>If set by the caller to FILL_WITH_DEFAULTS, then the spooler will fill <i>pAttributeInfo</i> with default values from level 1 up to the level specified by <i>dwLevel</i>.</p>
<p>For example, if <i>dwLevel</i> is 4 and FILL_WITH_DEFAULTS is specified, <i>pAttributeInfo</i> will be filled with the following default member values of <a href="..\winddiui\ns-winddiui--attribute-info-4.md">ATTRIBUTE_INFO_4</a>:</p>
<p><b>dwJobNumberOfPagesPerSide</b> = 1</p>
<p><b>dwDrvNumberOfPagesPerSide</b> = 1</p>
<p><b>dwNupBorderFlags</b> = 0</p>
<p><b>dwJobPageOrderFlags</b> = 0</p>
<p><b>dwDrvPageOrderFlags</b> = 0</p>
<p><b>dwJobNumberOfCopies</b> = <b>dmCopies</b> member of <a href="display.devmodew">DEVMODEW</a>
</p>
<p><b>dwDrvNumberOfCopies</b>  = <b>dmCopies</b> member of DEVMODEW</p>
<p><b>dwColorOptimization</b> = 0</p>
<p><b>dmPrintQuality</b> = <b>dmPrintQuality</b> member of DEVMODEW</p>
<p><b>dmYResolution</b> = <b>dmYResolution</b> member of DEVMODEW</p>
<p><b>dwNupDirection</b> = RIGHT_THEN_DOWN</p>
<p><b>dwBookletFlags </b>= BOOKLET_EDGE_LEFT</p>
<p><b>dwDuplexFlags </b>= 0</p>
<p><b>dwScalingPercentX </b>= 100</p>
<p><b>dwScalingPercentY </b>= 100</p>
<p><b>dwJobHandlingFlags </b>= 0</p>
<p>See Remarks.</p>
</dd>
</dl>

## -returns
<p><b>GetJobAttributesEx</b> returns <b>TRUE</b> if it is successful in obtaining the print job attributes; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>This function first checks whether the driver supports the attribute level that is indicated by <i>dwLevel</i>. If the driver does not support that attribute level, then the function queries the driver for support for the next lower level, (<i>dwLevel</i> - 1), and continues to query for progressively lower levels of support until it obtains the level of support provided by the driver. If <i>dwFlags</i> is set to FILL_WITH_DEFAULTS, then the function fills in the default values for the unsupported levels.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This function is available in the Windows Vista operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
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
<a href="..\winsplp\nf-winsplp-getjobattributes.md">GetJobAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20GetJobAttributesEx function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
