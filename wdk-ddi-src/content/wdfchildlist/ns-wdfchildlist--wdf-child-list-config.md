---
UID: NS.wdfchildlist._WDF_CHILD_LIST_CONFIG
title: WDF_CHILD_LIST_CONFIG
author: windows-driver-content
description: The WDF_CHILD_LIST_CONFIG structure contains configuration information for a list of child devices.
old-location: wdf\wdf_child_list_config.htm
old-project: wdf
ms.assetid: d0a392f4-c7c3-4b61-960c-b94f9605f5a4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_CHILD_LIST_CONFIG, WDF_CHILD_LIST_CONFIG, *PWDF_CHILD_LIST_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_LIST_CONFIG
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_LIST_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_LIST_CONFIG</b> structure contains configuration information for a list of child devices. </p>


## -syntax

````
typedef struct _WDF_CHILD_LIST_CONFIG {
  ULONG                                                   Size;
  ULONG                                                   IdentificationDescriptionSize;
  ULONG                                                   AddressDescriptionSize;
  PFN_WDF_CHILD_LIST_CREATE_DEVICE                        EvtChildListCreateDevice;
  PFN_WDF_CHILD_LIST_SCAN_FOR_CHILDREN                    EvtChildListScanForChildren;
  PFN_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COPY      EvtChildListIdentificationDescriptionCopy;
  PFN_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE EvtChildListIdentificationDescriptionDuplicate;
  PFN_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_CLEANUP   EvtChildListIdentificationDescriptionCleanup;
  PFN_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COMPARE   EvtChildListIdentificationDescriptionCompare;
  PFN_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY             EvtChildListAddressDescriptionCopy;
  PFN_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_DUPLICATE        EvtChildListAddressDescriptionDuplicate;
  PFN_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP          EvtChildListAddressDescriptionCleanup;
  PFN_WDF_CHILD_LIST_DEVICE_REENUMERATED                  EvtChildListDeviceReenumerated;
} WDF_CHILD_LIST_CONFIG, *PWDF_CHILD_LIST_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>IdentificationDescriptionSize</b>

<dd>
<p>The size, in bytes, of each child's <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">identification description</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>.</p>
</dd>

### -field <b>AddressDescriptionSize</b>

<dd>
<p>The size, in bytes, of each child's <a href="wdf.dynamic_enumeration#dynamic_child_descriptions#dynamic_child_descriptions">address description</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>.</p>
</dd>

### -field <b>EvtChildListCreateDevice</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> event callback function. This callback function is required.</p>
</dd>

### -field <b>EvtChildListScanForChildren</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-scan-for-children.md">EvtChildListScanForChildren</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListIdentificationDescriptionCopy</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-copy.md">EvtChildListIdentificationDescriptionCopy</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListIdentificationDescriptionDuplicate</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-duplicate.md">EvtChildListIdentificationDescriptionDuplicate</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListIdentificationDescriptionCleanup</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-cleanup.md">EvtChildListIdentificationDescriptionCleanup</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListIdentificationDescriptionCompare</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md">EvtChildListIdentificationDescriptionCompare</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListAddressDescriptionCopy</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-copy.md">EvtChildListAddressDescriptionCopy</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListAddressDescriptionDuplicate</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md">EvtChildListAddressDescriptionDuplicate</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListAddressDescriptionCleanup</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-cleanup.md">EvtChildListAddressDescriptionCleanup</a> event callback function. This callback function is optional.</p>
</dd>

### -field <b>EvtChildListDeviceReenumerated</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-device-reenumerated.md">EvtChildListDeviceReenumerated</a> event callback function. This callback function is optional.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_CHILD_LIST_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a> methods.</p>

<p>To initialize a WDF_CHILD_LIST_CONFIG structure, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551228">WDF_CHILD_LIST_CONFIG_INIT</a>.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551228">WDF_CHILD_LIST_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_LIST_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
