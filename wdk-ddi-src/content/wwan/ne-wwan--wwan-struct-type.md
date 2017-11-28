---
UID: NE.wwan._WWAN_STRUCT_TYPE
title: WWAN_STRUCT_TYPE
author: windows-driver-content
description: The WWAN_STRUCT_TYPE enumeration lists the different types of the list elements that follow the WWAN_LIST_HEADER object in memory.
old-location: netvista\wwan_struct_type.htm
old-project: netvista
ms.assetid: 43729964-9338-45ab-ad59-406176c1ae9f
ms.author: windowsdriverdev
ms.date: 11/22/2017
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

### -field <a id="WwanStructTN"></a><a id="wwanstructtn"></a><a id="WWANSTRUCTTN"></a><b>WwanStructTN</b>

<dd>
<p>The elements are NULL-terminated strings of Telephone Number (TNs), with each string having
     WWAN_TN_LEN characters.
     </p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569833">OID_WWAN_READY_INFO</a> uses this value to
     represent a list of TNs assigned to the device.</p>
</dd>

### -field <a id="WwanStructContext"></a><a id="wwanstructcontext"></a><a id="WWANSTRUCTCONTEXT"></a><b>WwanStructContext</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571201">WWAN_CONTEXT</a>.
     </p>
<p>
<a href="netvista.oid_wwan_provisioned_contexts">
     OID_WWAN_PROVISIONED_CONTEXTS</a> uses this value to represent a list of provisioned
     contexts.</p>
</dd>

### -field <a id="WwanStructProvider"></a><a id="wwanstructprovider"></a><a id="WWANSTRUCTPROVIDER"></a><b>WwanStructProvider</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571223">WWAN_PROVIDER</a>.
     </p>
<p>Both <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a> use this
     value to represent a list of network providers for WWAN 1.0 miniport drivers.</p>
</dd>

### -field <a id="WwanStructSmsPdu"></a><a id="wwanstructsmspdu"></a><a id="WWANSTRUCTSMSPDU"></a><b>WwanStructSmsPdu</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571248">WWAN_SMS_PDU_RECORD</a>.</p>
</dd>

### -field <a id="WwanStructReserved0"></a><a id="wwanstructreserved0"></a><a id="WWANSTRUCTRESERVED0"></a><b>WwanStructReserved0</b>

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanStructReserved1"></a><a id="wwanstructreserved1"></a><a id="WWANSTRUCTRESERVED1"></a><b>WwanStructReserved1</b>

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanStructReserved2"></a><a id="wwanstructreserved2"></a><a id="WWANSTRUCTRESERVED2"></a><b>WwanStructReserved2</b>

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanStructSmsCdma"></a><a id="wwanstructsmscdma"></a><a id="WWANSTRUCTSMSCDMA"></a><b>WwanStructSmsCdma</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>.</p>
</dd>

### -field <a id="WwanStructReserved3"></a><a id="wwanstructreserved3"></a><a id="WWANSTRUCTRESERVED3"></a><b>WwanStructReserved3</b>

<dd>
<p>The value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanStructDeviceServiceEntry"></a><a id="wwanstructdeviceserviceentry"></a><a id="WWANSTRUCTDEVICESERVICEENTRY"></a><b>WwanStructDeviceServiceEntry</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh831870">WWAN_DEVICE_SERVICE_ENTRY</a>.</p>
</dd>

### -field <a id="WwanStructProvider2"></a><a id="wwanstructprovider2"></a><a id="WWANSTRUCTPROVIDER2"></a><b>WwanStructProvider2</b>

<dd>
<p>The elements are of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh464135">WWAN_PROVIDER2</a>.</p>
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

### -field <a id="WwanStructDeviceServiceGuid"></a><a id="wwanstructdeviceserviceguid"></a><a id="WWANSTRUCTDEVICESERVICEGUID"></a><b>WwanStructDeviceServiceGuid</b>

<dd>
<p>The elements are of type 
     GUID.</p>
</dd>

### -field <a id="WwanStructDeviceServiceCommandId"></a><a id="wwanstructdeviceservicecommandid"></a><a id="WWANSTRUCTDEVICESERVICECOMMANDID"></a><b>WwanStructDeviceServiceCommandId</b>

<dd>
<p>The elements are of type ULONG.</p>
</dd>

### -field <a id="WwanStructDeviceCellularClass"></a><a id="wwanstructdevicecellularclass"></a><a id="WWANSTRUCTDEVICECELLULARCLASS"></a><b>WwanStructDeviceCellularClass</b>

<dd>
<p>The elements are of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff571199">WWAN_CELLULAR_CLASS</a>. </p>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569824">OID_WWAN_DEVICE_CAPS</a> uses this value to represent multiple cellular classes supported by the miniport driver.</p>
</dd>

### -field <a id="WwanStructMax"></a><a id="wwanstructmax"></a><a id="WWANSTRUCTMAX"></a><b>WwanStructMax</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571201">WWAN_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569831">OID_WWAN_PROVISIONED_CONTEXTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571223">WWAN_PROVIDER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571248">WWAN_SMS_PDU_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571208">WWAN_LIST_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_STRUCT_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
