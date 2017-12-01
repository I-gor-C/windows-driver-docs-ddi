---
UID: NS.iscsicfg._MSiSCSI_BootConfiguration
title: MSiSCSI_BootConfiguration
author: windows-driver-content
description: The MSiSCSI_BootConfiguration structure describes how the boot device is configured.
old-location: storage\msiscsi_bootconfiguration.htm
old-project: storage
ms.assetid: 3a4b55b1-977d-43fb-9968-7a734e04b21b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSiSCSI_BootConfiguration, MSiSCSI_BootConfiguration, *PMSiSCSI_BootConfiguration
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
req.alt-api: MSiSCSI_BootConfiguration
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
req.iface: 
---

# MSiSCSI_BootConfiguration structure



## -description
<p>The MSiSCSI_BootConfiguration structure describes how the boot device is configured. </p>


## -syntax

````
typedef struct _MSiSCSI_BootConfiguration {
  ULONGLONG          LUN;
  ULONGLONG          SecurityFlags;
  ULONG              UsernameSize;
  ULONG              PasswordSize;
  BOOLEAN            DiscoverBootDevice;
  WCHAR              InitiatorNode[223 + 1];
  WCHAR              TargetName[223 + 1];
  ISCSI_TargetPortal TargetPortal;
  ISCSI_LoginOptions LoginOptions;
  UCHAR              Username[1];
} MSiSCSI_BootConfiguration, *PMSiSCSI_BootConfiguration;
````


## -struct-fields
<dl>

### -field <b>LUN</b>

<dd>
<p>The logical unit number (LUN) that identifies the logical unit on the target that functions as a boot device.</p>
</dd>

### -field <b>SecurityFlags</b>

<dd>
<p>A bitwise OR of security flags that indicate the security requirements of the boot device. For a list of possible flags for this member, see <a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>.</p>
</dd>

### -field <b>UsernameSize</b>

<dd>
<p>The size, in bytes, of the string in <b>Username</b>.</p>
</dd>

### -field <b>PasswordSize</b>

<dd>
<p>The size, in bytes, of the string in <b>Password</b>.</p>
</dd>

### -field <b>DiscoverBootDevice</b>

<dd>
<p>A Boolean value that indicates whether the system should dynamically discover the boot device. If this member is <b>TRUE</b>, the system should dynamically discover the boot device. </p>
</dd>

### -field <b>InitiatorNode</b>

<dd>
<p>The iSCSI name of the initiator node to use for connecting to the boot device. If this member is <b>NULL</b>, the HBA can choose any initiator node. The iSCSI name for the initiator uniquely identifies the initiator anywhere in the world. For more information about how to specify this name, see the <i>iSCSI </i>specification that is published by the Internet Engineering Task Force (IETF) of the IP storage working group. </p>
</dd>

### -field <b>TargetName</b>

<dd>
<p>The iSCSI name for the target that contains the boot device.</p>
</dd>

### -field <b>TargetPortal</b>

<dd>
<p>A <a href="..\iscsidef\ns-iscsidef--iscsi-targetportal.md">ISCSI_TargetPortal</a> structure that specifies the portal to use for the connection.</p>
</dd>

### -field <b>LoginOptions</b>

<dd>
<p>A <a href="..\iscsidef\ns-iscsidef--iscsi-loginoptions.md">ISCSI_LoginOptions</a> structure that specifies the characteristics of the logon session to establish with the boot device.</p>
</dd>

### -field <b>Username</b>

<dd>
<p>A variable length array of characters that specifies the user name to use with the challenge handshake authentication protocol (CHAP). The user name is also known as the <i>CHAP name</i> (CHAP_N). The initiator uses the CHAP name to authenticate the target.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite automatically generates a declaration of the MSiSCSI_BootConfiguration structure when it compiles the <a href="storage.msiscsi_bootconfiguration_wmi_class">MSiSCSI_BootConfiguration WMI Class</a> in <i>Config.mof</i>.It is optional that you implement this class.</p>

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
<a href="..\iscsidef\ns-iscsidef--iscsi-loginoptions.md">ISCSI_LoginOptions</a>
</dt>
<dt>
<a href="..\iscsidef\ns-iscsidef--iscsi-targetportal.md">ISCSI_TargetPortal</a>
</dt>
<dt>
<a href="storage.msiscsi_bootconfiguration_wmi_class">MSiSCSI_BootConfiguration WMI Class</a>
</dt>
<dt>
<a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_BootConfiguration structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
