---
UID: NS.windot11.DOT11_DISASSOCIATION_PARAMETERS
title: DOT11_DISASSOCIATION_PARAMETERS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_disassociation_parameters.htm
old-project: netvista
ms.assetid: bf5f520e-4bbc-4b9f-9e6c-b430cb9e3b28
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_DISASSOCIATION_PARAMETERS, DOT11_DISASSOCIATION_PARAMETERS, *PDOT11_DISASSOCIATION_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_DISASSOCIATION_PARAMETERS
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_DISASSOCIATION_PARAMETERS structure



## -description

## -syntax

````
typedef struct DOT11_DISASSOCIATION_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  DOT11_MAC_ADDRESS  MacAddr;
  DOT11_ASSOC_STATUS uReason;
  ULONG              uIHVDataOffset;
  ULONG              uIHVDataSize;
} DOT11_DISASSOCIATION_PARAMETERS, *PDOT11_DISASSOCIATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_DISASSOCIATION_PARAMETERS structure. This member is
     formatted as an 
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
<p>This member must be set to DOT11_DISASSOCIATION_PARAMETERS_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       sizeof(DOT11_DISASSOCIATION_PARAMETERS).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>MacAddr</b>

<dd>
<p>The media access control (MAC) address of the AP or peer station that the 802.11 station has
     disassociated from.
     </p>
<p>If the miniport driver sets 
     <b>MacAddr</b> to the wildcard value of 0xFFFFFFFFFFFF, the 802.11 station has disassociated from the AP
     or all peer stations.</p>
</dd>

### -field <b>uReason</b>

<dd>
<p>The reason for the disassociation formatted as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547652">DOT11_ASSOC_STATUS</a> value.</p>
</dd>

### -field <b>uIHVDataOffset</b>

<dd>
<p>The offset of a block of data in a proprietary format that is defined by the IHV. The IHV can use
      this data block for any purposes that are related to the 
      <a href="netvista.ndis_status_dot11_disassociation">
      NDIS_STATUS_DOT11_DISASSOCIATION</a> status indication.</p>
<p>This offset is relative to the start of the buffer, which contains the
      DOT11_DISASSOCIATION_PARAMETERS structure.</p>
<p>If the miniport driver is not returning IHV data in the 
      NDIS_STATUS_DOT11_DISASSOCIATION indication, it must set uIHVDataOffset to
      zero.</p>
</dd>

### -field <b>uIHVDataSize</b>

<dd>
<p>The length of the block of data that is used by the IHV for the 
     <a href="netvista.ndis_status_dot11_disassociation">
     NDIS_STATUS_DOT11_DISASSOCIATION</a> status indication. If the miniport driver is not returning IHV
     data in this indication, it must set 
     <b>uIHVDataSize</b> to zero.</p>
</dd>
</dl>

## -remarks
<p>For more information about the disassociation operation, see 
    <a href="NULL">Disassociation Operations</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547652">DOT11_ASSOC_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_disassociation">
   NDIS_STATUS_DOT11_DISASSOCIATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_DISASSOCIATION_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
