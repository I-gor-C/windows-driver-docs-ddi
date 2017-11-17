---
UID: NS.wdfchildlist._WDF_CHILD_RETRIEVE_INFO
title: WDF_CHILD_RETRIEVE_INFO
author: windows-driver-content
description: The WDF_CHILD_RETRIEVE_INFO structure contains information about a child device that is obtained by calling WdfChildListRetrieveNextDevice or WdfChildListRetrievePdo.
old-location: wdf\wdf_child_retrieve_info.htm
ms.assetid: 0c48e7cd-e9aa-4ae7-bd44-fe16e1b0d619
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_RETRIEVE_INFO
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_CHILD_RETRIEVE_INFO, WDF_CHILD_RETRIEVE_INFO, *PWDF_CHILD_RETRIEVE_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_RETRIEVE_INFO structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The WDF_CHILD_RETRIEVE_INFO structure contains information about a child device that is obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a>.</p>


## -syntax

````
typedef struct _WDF_CHILD_RETRIEVE_INFO {
  ULONG                                                 Size;
  PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER          IdentificationDescription;
  PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER                 AddressDescription;
  WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS                 Status;
  PFN_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COMPARE EvtChildListIdentificationDescriptionCompare;
} WDF_CHILD_RETRIEVE_INFO, *PWDF_CHILD_RETRIEVE_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>IdentificationDescription</b>

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure. The driver must supply a value for this structure's <b>IdentificationDescriptionSize</b> member. </p>
<p>If the driver is calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> and supplying an <a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a> callback function, the driver must also provide an <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a> that the callback function can use to compare with an entry in a child list.</p>
<p>If the driver is calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a>, the driver must fill in the entire identification description.</p>
</dd>

### -field <b>AddressDescription</b>

<dd>
<p>A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure. The driver must supply a value for this structure's <b>AddressDescriptionSize</b> member. The framework fills in the rest of the <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">address description</a> when it retrieves a child from the child list. If the value of <b>AddressDescriptionSize</b> is <b>NULL</b>, address description information is not retrieved.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551233">WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</a>-typed value that the framework provides.</p>
</dd>

### -field <b>EvtChildListIdentificationDescriptionCompare</b>

<dd>
<p>A driver-supplied pointer to an <a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a> callback function. </p>
<p>If the driver is calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>, this pointer is optional and can be <b>NULL</b>. </p>
<p>If the driver is calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a>, this pointer is not used.</p>
</dd>
</dl>

## -remarks
<p>The WDF_CHILD_RETRIEVE_INFO structure is passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a> methods. </p>

<p>To initialize a WDF_CHILD_RETRIEVE_INFO structure, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551237">WDF_CHILD_RETRIEVE_INFO_INIT</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b807f9f8-588f-4303-be97-a9fd4cff2bbd">EvtChildListIdentificationDescriptionCompare</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551233">WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_RETRIEVE_INFO structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
