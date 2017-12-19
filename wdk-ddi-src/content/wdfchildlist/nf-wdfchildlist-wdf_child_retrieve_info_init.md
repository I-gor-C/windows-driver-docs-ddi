---
UID: NF.wdfchildlist.WDF_CHILD_RETRIEVE_INFO_INIT
title: WDF_CHILD_RETRIEVE_INFO_INIT function
author: windows-driver-content
description: The WDF_CHILD_RETRIEVE_INFO_INIT function initializes a WDF_CHILD_RETRIEVE_INFO structure.
old-location: wdf\wdf_child_retrieve_info_init.htm
old-project: wdf
ms.assetid: e41a656c-c507-45ca-a232-6926ace3c9d9
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WDF_CHILD_RETRIEVE_INFO_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_RETRIEVE_INFO_INIT
req.alt-loc: Wdfchildlist.h
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
req.product: Windows 10 or later.
---

# WDF_CHILD_RETRIEVE_INFO_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_CHILD_RETRIEVE_INFO_INIT</b> function initializes a <a href="wdf.wdf_child_retrieve_info">WDF_CHILD_RETRIEVE_INFO</a> structure.



## -syntax

````
VOID WDF_CHILD_RETRIEVE_INFO_INIT(
  _Out_ PWDF_CHILD_RETRIEVE_INFO                     Info,
  _In_  PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
);
````


## -parameters

### -param Info [out]

A pointer to a driver-supplied <a href="wdf.wdf_child_retrieve_info">WDF_CHILD_RETRIEVE_INFO</a> structure.


### -param IdentificationDescription [in]

A pointer to a driver-supplied <a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure.


## -returns
None

For a code example that uses <b>WDF_CHILD_RETRIEVE_INFO_INIT</b>, see <a href="wdf.wdfchildlistretrievenextdevice">WdfChildListRetrieveNextDevice</a>.


## -remarks


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
Header

</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_child_identification_description_header">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="wdf.wdf_child_retrieve_info">WDF_CHILD_RETRIEVE_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_RETRIEVE_INFO_INIT function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

