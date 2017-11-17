---
UID: NS.iscsiop._ISCSI_Persistent_Login
title: ISCSI_Persistent_Login
author: windows-driver-content
description: The ISCSI_Persistent_Login structure defines a persistent logon that the operating system initiates automatically when the computer boots up.
old-location: storage\iscsi_persistent_login.htm
ms.assetid: c43ee3dd-552a-41ab-9b4f-01611e44f453
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_Persistent_Login
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
ms.keywords: ISCSI_Persistent_Login, ISCSI_Persistent_Login, *PISCSI_Persistent_Login
req.iface: 
---

# ISCSI_Persistent_Login structure



## -description
<p>The ISCSI_Persistent_Login structure defines a persistent logon that the operating system initiates automatically when the computer boots up.</p>


## -syntax

````
typedef struct _ISCSI_Persistent_Login {
  WCHAR               TargetName[223 + 1];
  ULONGLONG           SecurityFlags;
  ULONG               InitiatorPortNumber;
  ULONG               UsernameSize;
  BOOLEAN             IsInformationalSession;
  USHORT              UniqueIdForISID;
  ISCSI_TargetPortal  TargetPortal;
  ISCSI_LoginOptions  LoginOptions;
  ISCSI_TargetMapping TargetMapping;
  UCHAR               Username[1];
} ISCSI_Persistent_Login, *PISCSI_Persistent_Login;
````


## -struct-fields
<dl>

### -field <b>TargetName</b>

<dd>
<p>A wide character string that indicates the name of the target with which the iSCSI initiator service establishes a persistent logon when it restarts.</p>
</dd>

### -field <b>SecurityFlags</b>

<dd>
<p>A bitwise OR of security flags that indicate the security requirements of the target that is specified in the persistent logon. For a list of possible values for this member, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565399">SECURITY_FLAG_QUALIFIERS</a>.</p>
</dd>

### -field <b>InitiatorPortNumber</b>

<dd>
<p>The port number on the initiator side to perform the logon operation through. </p>
</dd>

### -field <b>UsernameSize</b>

<dd>
<p>The size, in bytes, of the string in <b>Username</b>.</p>
</dd>

### -field <b>IsInformationalSession</b>

<dd>
<p>A Boolean value that indicates whether the persistent logon is configured to establish a purely informational session. If this member is <b>TRUE</b>, the persistent logon is configured to establish a purely informational session.</p>
</dd>

### -field <b>UniqueIdForISID</b>

<dd>
<p>Portal to use for initial connection</p>
</dd>

### -field <b>TargetPortal</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a> structure that specifies which target portal to use for the initial logon connection.</p>
</dd>

### -field <b>LoginOptions</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff561541">ISCSI_LoginOptions</a> structure that specifies the characteristics of the persistent logon session. </p>
</dd>

### -field <b>TargetMapping</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff561572">ISCSI_TargetMapping</a> structure that defines the target mappings. </p>
</dd>

### -field <b>Username</b>

<dd>
<p>A variable-length array of characters that specifies the challenge handshake authentication protocol user name (CHAP_N) to use when the initiator is authenticating the target. The number of elements in the array is specified by the <b>UsernameSize</b> field.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561556">ISCSI_Persistent_Login WMI Class</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561541">ISCSI_LoginOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561572">ISCSI_TargetMapping</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565399">SECURITY_FLAG_QUALIFIERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20ISCSI_Persistent_Login structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
