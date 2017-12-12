---
UID: NF.wdfstring.WdfStringGetUnicodeString
title: WdfStringGetUnicodeString function
author: windows-driver-content
description: The WdfStringGetUnicodeString method retrieves the Unicode string that is assigned to a specified framework string object.
old-location: wdf\wdfstringgetunicodestring.htm
old-project: wdf
ms.assetid: 39041953-11ef-4f31-9b7e-09ce40b6b930
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfStringGetUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfstring.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfStringGetUnicodeString
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfStringGetUnicodeString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfStringGetUnicodeString</b> method retrieves the Unicode string that is assigned to a specified framework string object.



## -syntax

````
VOID WdfStringGetUnicodeString(
  _In_  WDFSTRING       String,
  _Out_ PUNICODE_STRING UnicodeString
);
````


## -parameters

### -param String [in]

A handle to a framework string object.


### -param UnicodeString [out]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that receives a pointer to the Unicode string that is currently assigned to the string object that <i>String</i> specifies.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
After <b>WdfStringGetUnicodeString</b> returns, the UNICODE_STRING structure that <i>UnicodeString</i> points to contains a pointer to the specified string object's Unicode string, along with the string's length. The Unicode string is allocated in paged pool.

 The framework does not make a copy of the string for the driver.

For more information about framework string objects, see <a href="wdf.using_string_objects">Using String Objects</a>.

The following code example obtains the Unicode string that is assigned to a specified framework string object.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfstring.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="wdf.wdfstringcreate">WdfStringCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfStringGetUnicodeString method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

