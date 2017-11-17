---
UID: NS.windot11.DOT11_BYTE_ARRAY
title: DOT11_BYTE_ARRAY
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_byte_array.htm
ms.assetid: a2c67eaf-d39e-43c9-8e06-18f668c0baa3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_BYTE_ARRAY
req.alt-loc: windot11.h
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
ms.keywords: DOT11_BYTE_ARRAY, DOT11_BYTE_ARRAY, *PDOT11_BYTE_ARRAY
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_BYTE_ARRAY structure



## -description

## -syntax

````
typedef struct DOT11_BYTE_ARRAY {
  NDIS_OBJECT_HEADER Header;
  ULONG              uNumOfBytes;
  ULONG              uTotalNumOfBytes;
  UCHAR              ucBuffer[1];
} DOT11_BYTE_ARRAY, *PDOT11_BYTE_ARRAY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_BYTE_ARRAY structure. This member is formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b>

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b>

<dd>
<p>This member must be set to the revision of the variable-length structures which follow the
       DOT11_BYTE_ARRAY structure. For more information about the revision of these structures, refer to the
       object identifiers (OIDS) listed in the 
       "See Also" section.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       sizeof(DOT11_BYTE_ARRAY).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uNumOfBytes</b>

<dd>
<p>The number of bytes in the 
     <b>ucBuffer</b> array.</p>
</dd>

### -field <b>uTotalNumOfBytes</b>

<dd>
<p>The maximum number of bytes that the 
     <b>ucBuffer</b> array requires.</p>
</dd>

### -field <b>ucBuffer</b>

<dd>
<p>The list of variable-length structures.</p>
</dd>
</dl>

## -remarks
<p>The type of structures stored in the 
    <b>ucBuffer</b> array depends on the OID set and query request. For example, when queried by 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569360">OID_DOT11_ENUM_BSS_LIST</a>, a miniport
    driver stores one or more DOT11_BSS_ENTRY structures in the 
    <b>ucBuffer</b> array.</p>

<p>When queried by an OID that uses the DOT11_BYTE_ARRAY structure, the miniport driver must verify that
    the 
    <b>InformationBuffer</b> member of the 
    <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function's
    <i>OidRequest</i> parameter is large enough to return the entire structure, including all entries in the 
    <b>ucBuffer</b> array. The value of the 
    <b>InformationBufferLength</b> member of the 
    <i>OidRequest</i> parameter determines what the miniport driver must do, as the following list shows:</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is less than the length, in bytes, of the entire DOT11_BYTE_ARRAY
      structure, the miniport driver must do the following:</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesWritten</b> member to zero and the 
        <b>BytesNeeded</b> member to the length, in bytes, of the entire DOT11_BYTE_ARRAY structure</p>

<p>Fail the query request by returning NDIS_STATUS_BUFFER_OVERFLOW from its 
        <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is greater than or equal to the length, in bytes, of the entire
      DOT11_BYTE_ARRAY structure, the miniport driver must do the following to complete a successful query
      request:</p>

<p>For the DOT11_BYTE_ARRAY structure, set the 
        <b>uNumOfBytes</b> and 
        <b>uTotalNumOfBytes</b> members to the total number of entries in the 
        <b>ucBuffer</b> array.</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesNeeded</b> member to zero and the 
        <b>BytesWritten</b> member to the length, in bytes, of the entire DOT11_BYTE_ARRAY structure. The
        miniport driver must also copy the entire DOT11_BYTE_ARRAY structure to the 
        <b>InformationBuffer</b> member.</p>

<p>Return NDIS_STATUS_SUCCESS from its 
        <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_dot11_cipher_key_mapping_key">
   OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569360">OID_DOT11_ENUM_BSS_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_BYTE_ARRAY structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
