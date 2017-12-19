---
UID: NS.ISCSIOP._LOGINTOTARGET_IN
title: _LoginToTarget_IN
author: windows-driver-content
description: The LoginToTarget_IN structure holds the input data for the LoginToTarget method, which is used to login to a target.
old-location: storage\logintotarget_in.htm
old-project: storage
ms.assetid: f25b503b-0182-452d-8561-b3c82f595f81
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _LoginToTarget_IN, *PLoginToTarget_IN, PLoginToTarget_IN, LoginToTarget_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LoginToTarget_IN
req.alt-loc: iscsiop.h
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

# _LoginToTarget_IN structure



## -description
The LoginToTarget_IN structure holds the input data for the <a href="storage.logintotarget">LoginToTarget</a> method, which is used to login to a target.



## -syntax

````
typedef struct _LoginToTarget_IN {
  ULONG               PortNumber;
  ISCSI_LoginOptions  LoginOptions;
  ULONG               SessionType;
  ULONGLONG           SecurityFlags;
  ISCSI_TargetPortal  TargetPortal;
  ULONG               UsernameSize;
  ULONG               PasswordSize;
  ULONG               KeySize;
  USHORT              UniqueIdForISID;
  BOOLEAN             PersistentLogin;
  WCHAR               InitiatorNode[223 + 1];
  WCHAR               InitiatorAlias[255 + 1];
  WCHAR               TargetName[223 + 1];
  ISCSI_TargetMapping Mappings;
  UCHAR               Key[1];
} LoginToTarget_IN, *PLoginToTarget_IN;
````


## -struct-fields

### -field PortNumber

The number of the port (initiator portal) that the HBA initiator uses to establish the logon session. This value must match the <b>Index</b> member of the <a href="storage.iscsi_portalinfo">ISCSI_PortalInfo</a> structure.


### -field LoginOptions

A <a href="storage.iscsi_loginoptions">ISCSI_LoginOptions</a> structure that specifies the characteristics of the logon session.


### -field SessionType

A <a href="storage.loginsessiontype">LOGINSESSIONTYPE</a> enumeration value that specifies the type of logon session. 


### -field SecurityFlags

A bitwise OR of security flags that indicate the security requirements that are associated with the authentication key that is used to establish the logon session. For a list of the flags that you can combine to define this member's value, see <a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>.


### -field TargetPortal

A <a href="storage.iscsi_targetportal">ISCSI_TargetPortal</a> structure that indicates which target portal to use to make the connection. 


### -field UsernameSize

The size, in bytes, of the string in <b>Username</b>.


### -field PasswordSize

The size, in bytes, of the string in <b>Password</b>.


### -field KeySize

The size, in bytes, of the string in <b>Key</b>.


### -field UniqueIdForISID

A number that the miniport driver that manages the HBA can use to construct a unique session identifier (ISID). 


### -field PersistentLogin

A Boolean value that indicates if the logon should be persistent. If this member is <b>TRUE</b>, the logon should be persistent. The HBA's miniport driver should store the characteristics of this logon in non-volatile memory and log on to the target automatically every time the operating system loads the miniport driver. If this member is <b>FALSE</b>, the logon is not persistent.


### -field InitiatorNode

The iSCSI name of the initiator node to use for the connection. If this member is empty, the HBA's miniport driver can choose any initiator node name during authentication. The initiator node name is usually an iSCSI qualified name (IQN).


### -field InitiatorAlias

The iSCSI alias of the initiator node. 


### -field TargetName

The iSCSI target name with which to establish the logon session. 


### -field Mappings

A <a href="storage.iscsi_targetmapping">ISCSI_TargetMapping</a> structure that maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI LUNs. If the initiator service does not specify mappings, the HBA's miniport driver can use any mappings for the LUNs. The miniport driver should report unmapped LUNs to the port driver to be enumerated.


### -field Key

A variable-length array of UCHAR values that defines the preshared key that is associated with the target IP address.


## -remarks
You must implement this method.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.iscsi_loginoptions">ISCSI_LoginOptions</a>
</dt>
<dt>
<a href="storage.iscsi_portalinfo">ISCSI_PortalInfo</a>
</dt>
<dt>
<a href="storage.iscsi_targetmapping">ISCSI_TargetMapping</a>
</dt>
<dt>
<a href="storage.iscsi_targetportal">ISCSI_TargetPortal</a>
</dt>
<dt>
<a href="storage.loginsessiontype">LOGINSESSIONTYPE</a>
</dt>
<dt>
<a href="storage.logintotarget">LoginToTarget</a>
</dt>
<dt>
<a href="storage.logintotarget_out">LoginToTarget_OUT</a>
</dt>
<dt>
<a href="storage.msiscsi_operations_wmi_class">MSiSCSI_Operations WMI Class</a>
</dt>
<dt>
<a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20LoginToTarget_IN structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

