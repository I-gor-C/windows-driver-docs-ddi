---
UID: NF.wdfchildlist.WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT
title: WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT
author: windows-driver-content
description: The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure.
old-location: wdf\wdf_child_identification_description_header_init.htm
ms.assetid: 5c0d7abf-05e3-45fc-b5a4-db6f79a94a87
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT
req.alt-loc: wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
ms.keywords: WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure.</p>


## -syntax

````
VOID WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT(
  _Out_ PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER Header,
  _In_  ULONG                                        IdentificationDescriptionSize
);
````


## -parameters
<dl>

### -param <i>Header</i> [out]

<dd>
<p>A pointer to a driver-allocated WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure.</p>
</dd>

### -param <i>IdentificationDescriptionSize</i> [in]

<dd>
<p>The size, in bytes, of a driver-defined structure that contains device identification information. For more information about specifying the size value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure and sets the structure's <b>IdentificationDescriptionSize</b> member to the specified value.</p>

<p>For more information about child identification descriptions, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.</p>

<p>The <b>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure and sets the structure's <b>IdentificationDescriptionSize</b> member to the specified value.</p>

<p>For more information about child identification descriptions, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545591">WdfChildListAddOrUpdateChildDescriptionAsPresent</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
