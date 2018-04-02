---
UID: NS:iscsiop._LoginToTarget_IN
title: "_LoginToTarget_IN"
author: windows-driver-content
description: The LoginToTarget_IN structure holds the input data for the LoginToTarget method, which is used to login to a target.
old-location: storage\logintotarget_in.htm
old-project: storage
ms.assetid: f25b503b-0182-452d-8561-b3c82f595f81
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PLoginToTarget_IN, LoginToTarget_IN, LoginToTarget_IN structure [Storage Devices], PLoginToTarget_IN, PLoginToTarget_IN structure pointer [Storage Devices], _LoginToTarget_IN, iscsiop/LoginToTarget_IN, iscsiop/PLoginToTarget_IN, storage.logintotarget_in, structs-iSCSI_b6201f88-03aa-41bf-a92b-eb9e95103911.xml"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	iscsiop.h
api_name:
-	LoginToTarget_IN
product:
- Windows
targetos: Windows
req.typenames: LoginToTarget_IN, *PLoginToTarget_IN
---

# _LoginToTarget_IN structure
The LoginToTarget_IN structure holds the input data for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a> method, which is used to login to a target.

## Syntax
```
typedef struct _LoginToTarget_IN {
  ULONG               PortNumber;
  ISCSI_LoginOptions  LoginOptions;
  ULONG               SessionType;
  ULONGLONG           SecurityFlags;
  ISCSI_TargetPortal  TargetPortal;
  ULONG               UsernameSize;
  ULONG               PasswordSize;
  ULONG               KeySize;
  USHORT              UniqueIdForISID;
  BOOLEAN             PersistentLogin;
  WCHAR               InitiatorNode[223 + 1];
  WCHAR               InitiatorAlias[255 + 1];
  WCHAR               TargetName[223 + 1];
  ISCSI_TargetMapping Mappings;
  UCHAR               Key[1];
} LoginToTarget_IN, *PLoginToTarget_IN;
```

## Members


`PortNumber`

The number of the port (initiator portal) that the HBA initiator uses to establish the logon session. This value must match the <b>Index</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561557">ISCSI_PortalInfo</a> structure.

`LoginOptions`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561541">ISCSI_LoginOptions</a> structure that specifies the characteristics of the logon session.

`SessionType`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561598">LOGINSESSIONTYPE</a> enumeration value that specifies the type of logon session.

`SecurityFlags`

A bitwise OR of security flags that indicate the security requirements that are associated with the authentication key that is used to establish the logon session. For a list of the flags that you can combine to define this member's value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565399">SECURITY_FLAG_QUALIFIERS</a>.

`TargetPortal`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a> structure that indicates which target portal to use to make the connection.

`UsernameSize`

The size, in bytes, of the string in <b>Username</b>.

`PasswordSize`

The size, in bytes, of the string in <b>Password</b>.

`KeySize`

The size, in bytes, of the string in <b>Key</b>.

`UniqueIdForISID`

A number that the miniport driver that manages the HBA can use to construct a unique session identifier (ISID).

`PersistentLogin`

A Boolean value that indicates if the logon should be persistent. If this member is <b>TRUE</b>, the logon should be persistent. The HBA's miniport driver should store the characteristics of this logon in non-volatile memory and log on to the target automatically every time the operating system loads the miniport driver. If this member is <b>FALSE</b>, the logon is not persistent.

`InitiatorNode`

The iSCSI name of the initiator node to use for the connection. If this member is empty, the HBA's miniport driver can choose any initiator node name during authentication. The initiator node name is usually an iSCSI qualified name (IQN).

`InitiatorAlias`

The iSCSI alias of the initiator node.

`TargetName`

The iSCSI target name with which to establish the logon session.

`Mappings`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561572">ISCSI_TargetMapping</a> structure that maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI LUNs. If the initiator service does not specify mappings, the HBA's miniport driver can use any mappings for the LUNs. The miniport driver should report unmapped LUNs to the port driver to be enumerated.

`Key`

A variable-length array of UCHAR values that defines the preshared key that is associated with the target IP address.

## Remarks
You must implement this method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iscsiop.h (include Iscsiop.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561541">ISCSI_LoginOptions</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561557">ISCSI_PortalInfo</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561572">ISCSI_TargetMapping</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561598">LOGINSESSIONTYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561601">LoginToTarget_OUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563091">MSiSCSI_Operations WMI Class</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff565399">SECURITY_FLAG_QUALIFIERS</a>