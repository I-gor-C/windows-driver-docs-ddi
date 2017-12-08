---
UID: NE.wwan._WWAN_STRUCT_TYPE
title: WWAN_STRUCT_TYPE
author: windows-driver-content
description: The WWAN_STRUCT_TYPE enumeration lists the different types of the list elements that follow the WWAN_LIST_HEADER object in memory.
old-location: netvista\wwan_struct_type.htm
old-project: netvista
ms.assetid: 43729964-9338-45ab-ad59-406176c1ae9f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_STRUCT_TYPE
req.alt-loc: wwan.h
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

# WWAN_STRUCT_TYPE enumeration



## -description
<p>The WWAN_STRUCT_TYPE enumeration lists the different types of the list elements that follow the
  WWAN_LIST_HEADER object in memory.</p>


## -syntax

````
typedef enum _WWAN_STRUCT_TYPE { 
  WwanStructTN                      = 0,
  WwanStructContext,
  WwanStructProvider,
  WwanStructSmsPdu,
  WwanStructReserved0,
  WwanStructReserved1,
  WwanStructReserved2,
  WwanStructSmsCdma,
  WwanStructReserved3,
  WwanStructDeviceServiceEntry,
  WwanStructProvider2,
  WwanStructDeviceServiceGuid,
  WwanStructDeviceServiceCommandId,
  WwanStructDeviceCellularClass,
  WwanStructMax
} WWAN_STRUCT_TYPE, *PWWAN_STRUCT_TYPE;
````


## -enum-fields
<dl>

### -field WwanStructTN

<dd>
<p>The elements are NULL-terminated strings of Telephone Number (TNs), with each string having
     WWAN_TN_LEN characters.
     </p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a> uses this value to
     represent a list of TNs assigned to the device.</p>
</dd>

### -field WwanStructContext

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-context.md">WWAN_CONTEXT</a>.
     </p>
<p>
<a href="netvista.oid_wwan_provisioned_contexts">
     OID_WWAN_PROVISIONED_CONTEXTS</a> uses this value to represent a list of provisioned
     contexts.</p>
</dd>

### -field WwanStructProvider

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-provider.md">WWAN_PROVIDER</a>.
     </p>
<p>Both <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a> use this
     value to represent a list of network providers for WWAN 1.0 miniport drivers.</p>
</dd>

### -field WwanStructSmsPdu

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-sms-pdu-record.md">WWAN_SMS_PDU_RECORD</a>.</p>
</dd>

### -field WwanStructReserved0

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field WwanStructReserved1

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field WwanStructReserved2

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field WwanStructSmsCdma

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-sms-cdma-record.md">WWAN_SMS_CDMA_RECORD</a>.</p>
</dd>

### -field WwanStructReserved3

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field WwanStructDeviceServiceEntry

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-device-service-entry.md">WWAN_DEVICE_SERVICE_ENTRY</a>.</p>
</dd>

### -field WwanStructProvider2

<dd>
<p>The elements are of type 
     <a href="..\wwan\ns-wwan--wwan-provider2.md">WWAN_PROVIDER2</a>.</p>
<p>The following OIDs use this value to represent a list of network providers for WWAN 2.0 miniport drivers:</p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a>
</p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a>
</p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831868">OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS</a>
</p>
</dd>

### -field WwanStructDeviceServiceGuid

<dd>
<p>The elements are of type 
     GUID.</p>
</dd>

### -field WwanStructDeviceServiceCommandId

<dd>
<p>The elements are of type ULONG.</p>
</dd>

### -field WwanStructDeviceCellularClass

<dd>
<p>The elements are of type <a href="..\wwan\ne-wwan--wwan-cellular-class.md">WWAN_CELLULAR_CLASS</a>. </p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a> uses this value to represent multiple cellular classes supported by the miniport driver.</p>
</dd>

### -field WwanStructMax

<dd>
<p>The total number of supported types.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-context.md">WWAN_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569831">OID_WWAN_PROVISIONED_CONTEXTS</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-provider.md">WWAN_PROVIDER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-pdu-record.md">WWAN_SMS_PDU_RECORD</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-cdma-record.md">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_STRUCT_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
