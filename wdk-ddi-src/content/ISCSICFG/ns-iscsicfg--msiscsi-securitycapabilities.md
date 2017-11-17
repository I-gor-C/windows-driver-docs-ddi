---
UID: NS.iscsicfg._MSiSCSI_SecurityCapabilities
title: MSiSCSI_SecurityCapabilities
author: windows-driver-content
description: The MSiSCSI_SecurityCapabilities structure describes the security capabilities of an initiator.
old-location: storage\msiscsi_securitycapabilities.htm
ms.assetid: a385283a-7b24-43aa-b291-541bfd6a91a6
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsicfg.h
req.include-header: Iscsicfg.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_SecurityCapabilities
req.alt-loc: iscsicfg.h
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
ms.keywords: MSiSCSI_SecurityCapabilities, MSiSCSI_SecurityCapabilities, *PMSiSCSI_SecurityCapabilities
req.iface: 
---

# MSiSCSI_SecurityCapabilities structure



## -description
<p>The MSiSCSI_SecurityCapabilities structure describes the security capabilities of an initiator. </p>


## -syntax

````
typedef struct _MSiSCSI_SecurityCapabilities {
  BOOLEAN ProtectiScsiTraffic;
  BOOLEAN ProtectiSNSTraffic;
  BOOLEAN CertificatesSupported;
  ULONG   EncryptionAvailableCount;
  ULONG   EncryptionAvailable[1];
} MSiSCSI_SecurityCapabilities, *PMSiSCSI_SecurityCapabilities;
````


## -struct-fields
<dl>

### -field <b>ProtectiScsiTraffic</b>

<dd>
<p>A Boolean value that indicates whether the initiator can use IPsec to protect iSCSI traffic. If this member is <b>TRUE</b>, the initiator can use IPsec to protect iSCSI traffic. If <b>FALSE</b>, the initiator cannot use IPsec.</p>
</dd>

### -field <b>ProtectiSNSTraffic</b>

<dd>
<p>A Boolean value that indicates whether the initiator can use IPsec to protect iSNS traffic. If this member is <b>TRUE</b>, the initiator can use IPsec to protect iSNS traffic. If <b>FALSE</b>, the initiator cannot use IPsec.</p>
</dd>

### -field <b>CertificatesSupported</b>

<dd>
<p>A Boolean value that indicates whether the initiator supports certificates. If this member is <b>TRUE</b>, the initiator supports certificates. If this member is <b>FALSE</b>, the initiatiator does not support certificates.</p>
</dd>

### -field <b>EncryptionAvailableCount</b>

<dd>
<p>The number of encryption types that the initiator supports. </p>
</dd>

### -field <b>EncryptionAvailable</b>

<dd>
<p>A variable length array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561528">ISCSI_ENCRYPTION_TYPES</a> structures, which indicate types of encryption that the initiator supports. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite automatically generates a declaration of the MSiSCSI_SecurityCapabilities structure when it compiles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563131">MSiSCSI_SecurityCapabilities WMI Class</a> in <i>Config.mof</i>. </p>

<p>Initiators that support IPsec must implement the MSiSCSI_SecurityCapabilities class. </p>

<p>Initiators must register the MSiSCSI_SecurityCapabilities class using the name of the physical device object (PDO) for the HBA. You must implement this class if the adapter supports IPsec.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsicfg.h (include Iscsicfg.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561528">ISCSI_ENCRYPTION_TYPES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563131">MSiSCSI_SecurityCapabilities WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSiSCSI_SecurityCapabilities structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
