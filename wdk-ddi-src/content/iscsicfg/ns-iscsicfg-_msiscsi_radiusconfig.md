---
UID: NS.ISCSICFG._MSISCSI_RADIUSCONFIG
title: _MSiSCSI_RADIUSConfig
author: windows-driver-content
description: The MSiSCSI_RADIUSConfig structure provides information that the initiator requires to use the remote authentication dial-in user service (RADIUS).
old-location: storage\msiscsi_radiusconfig.htm
old-project: storage
ms.assetid: 6f8be86e-2729-4aa9-982d-df323f05cf1c
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _MSiSCSI_RADIUSConfig, *PMSiSCSI_RADIUSConfig, MSiSCSI_RADIUSConfig
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsicfg.h
req.include-header: Iscsicfg.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_RADIUSConfig
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
---

# _MSiSCSI_RADIUSConfig structure



## -description
The MSiSCSI_RADIUSConfig structure provides information that the initiator requires to use the remote authentication dial-in user service (RADIUS).



## -syntax

````
typedef struct _MSiSCSI_RADIUSConfig {
  BOOLEAN          UseRADIUSForCHAP;
  ULONG            SharedSecretSizeInBytes;
  ISCSI_IP_Address RADIUSServer;
  ISCSI_IP_Address BackupRADIUSServer;
  ULONG            Reserved;
  UCHAR            SharedSecret[1];
} MSiSCSI_RADIUSConfig, *PMSiSCSI_RADIUSConfig;
````


## -struct-fields

### -field UseRADIUSForCHAP

A Boolean value that indicates whether the initiator should use RADIUS for authentication during the challenge handshake of the challenge handshake authentication protocol (CHAP). If this member is <b>TRUE</b>, the initiator should use RADIUS for authentication during the challenge handshake of CHAP. If this member is <b>FALSE</b>, the initiator is not required to use RADIUS.


### -field SharedSecretSizeInBytes

The size, in bytes, of shared secret for use with RADIUS servers.


### -field RADIUSServer

A <a href="storage.iscsi_ip_address">ISCSI_IP_Address</a> structure that specifies a fixed address for the RADIUS server. The ISCSI_IP_Address structure defines the IP address in a way that is independent of the version of the IP protocol in use. 


### -field BackupRADIUSServer

A ISCSI_IP_Address structure that specifies a fixed addresses for a backup RADIUS server. 


### -field Reserved

Reserved for Microsoft use only. Set this member to zero.


### -field SharedSecret

A variable-length array that contains a shared secret. The initiator uses this shared secret to authenticate primary and backup RADIUS servers.


## -remarks
Initiators use RADIUS servers to perform authentication during the challenge handshake of CHAP.

The WMI tool suite automatically generates a declaration of the MSiSCSI_RADIUSConfig structure when it compiles the <a href="storage.msiscsi_radiusconfig_wmi_class">MSiSCSI_RADIUSConfig WMI Class</a> in <i>Config.mof</i>. 

Initiators that support using RADIUS for CHAP authentication must implement the MSiSCSI_RADIUSConfig class.

Initiators should use RADIUS whenever possible, because RADIUS allows the centralized management of CHAP credentials. 

Initiators should register each instance of the MSiSCSI_RADIUSConfig class using the name of the physical device object (PDO) for the HBAYou must implement this class if the adapter supports authentication via RADIUS.


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="storage.iscsi_ip_address">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="storage.msiscsi_radiusconfig_wmi_class">MSiSCSI_RADIUSConfig WMI Class</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_RADIUSConfig structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

