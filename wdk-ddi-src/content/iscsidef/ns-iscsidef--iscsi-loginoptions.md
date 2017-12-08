---
UID: NS.iscsidef._ISCSI_LoginOptions
title: ISCSI_LoginOptions
author: windows-driver-content
description: The ISCSI_LoginOptions structure defines the characteristics of a logon session. The LoginToTarget_IN routines use these defined characteristics while it logs into an iSCSI target.
old-location: storage\iscsi_loginoptions.htm
old-project: storage
ms.assetid: 2440999a-e10c-4a27-b076-a0b640c2ca7f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_LoginOptions, ISCSI_LoginOptions, *PISCSI_LoginOptions
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsidef.h
req.include-header: Iscsidef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_LoginOptions
req.alt-loc: iscsidef.h
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

# ISCSI_LoginOptions structure



## -description
<p>The ISCSI_LoginOptions structure defines the characteristics of a logon session. The LoginToTarget_IN routines use these defined characteristics while it logs into an iSCSI target.</p>


## -syntax

````
typedef struct _ISCSI_LoginOptions {
  ULONG InformationSpecified;
  ULONG HeaderDigest;
  ULONG DataDigest;
  ULONG MaximumConnections;
  ULONG DefaultTime2Wait;
  ULONG DefaultTime2Retain;
  ULONG LoginFlags;
  ULONG AuthType;
} ISCSI_LoginOptions, *PISCSI_LoginOptions;
````


## -struct-fields
<dl>

### -field InformationSpecified

<dd>
<p>A bitmap that indicates which members of the ISCSI_LoginOptions structure contain valid data. The following table describes the possible values: </p>
<table>
<tr>
<th>Bit</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_HEADER_DIGEST</p>
</td>
<td>
<p>The <b>HeaderDigest</b> member specifies the type of digest that is used to guarantee the integrity of header data. </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_DATA_DIGEST</p>
</td>
<td>
<p>The <b>DataDigest</b> member specifies the type of digest that is used to guarantee the integrity of header data.</p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS</p>
</td>
<td>
<p>The <b>MaximumConnections</b> member specifies the maximum number of connections that are allowed in the iSCSI session. </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT</p>
</td>
<td>
<p>The <b>DefaultTime2Wait</b> member specifies the minimum time to wait, in seconds, before the initiator attempts to reconnect or reassign a connection that was dropped. </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_RETAIN</p>
</td>
<td>
<p>The <b>DefaultTime2Retain</b> member specifies the maximum time that is allowed to reassign commands after the initial wait indicated in <b>DefaultTime2Wait</b>.</p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_AUTH_TYPE</p>
</td>
<td>
<p>The <b>AuthType</b> member specifies the type of authentication that establishes the logon session. </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_USERNAME</p>
</td>
<td>
<p>The username to be used during logon. </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_OPTIONS_PASSWORD</p>
</td>
<td>
<p>The password to be used during logon. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field HeaderDigest

<dd>
<p>A <a href="storage.iscsi_digest_types">ISCSI_DIGEST_TYPES</a> value that indicates the method that the initiator uses to verify the integrity of the header digest in a logon PDU.</p>
</dd>

### -field DataDigest

<dd>
<p>A <a href="storage.iscsi_digest_types">ISCSI_DIGEST_TYPES</a> value that indicates the method that the initiator uses to verify the integrity of the data digest in a logon PDU.</p>
</dd>

### -field MaximumConnections

<dd>
<p>A value between 1 and 65535 that specifies the maximum number of connections to target devices that can be associated with a single logon session. A value of 0 indicates that there is no limit to the number of connections. </p>
</dd>

### -field DefaultTime2Wait

<dd>
<p>The minimum time to wait, in seconds, before the initiator attempts to reconnect or reassign a connection (or task) that has been dropped after an unexpected connection termination or reset. The initiator and target negotiate to determine this value.</p>
</dd>

### -field DefaultTime2Retain

<dd>
<p>The maximum time, in seconds, to reassign a connection after the initial wait that is indicated in <b>DefaultTime2Wait</b> has elapsed. The initiator and target negotiate to determine this value.</p>
</dd>

### -field LoginFlags

<dd>
<p>A bitwise OR of logon flags that define certain characteristics of the logon session. The following table indicates the values that you can assign to this member.</p>
<table>
<tr>
<th>Logon flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_REQUIRE_IPSEC</p>
</td>
<td>
<p>The logon session must use the IPSec protocol.</p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED</p>
</td>
<td>
<p>Multipathing software is installed, so the iSCSI initiator service allows multiple sessions to the same target.  </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_RESERVED1</p>
</td>
<td>
<p>Microsoft internal use only.  </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING</p>
</td>
<td>
<p>If a target portal is not available for login, the initiator can "hop" through the list of target portals that it discovered and that can be used for login operations. That is, the initiator will continue to try the list of portals that are available until it finds one that can be used for login, so it can then log in to the available target portal.</p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_USE_RADIUS_RESPONSE</p>
</td>
<td>
<p>Use RADIUS to generate CHAP response.  </p>
</td>
</tr>
<tr>
<td>
<p>ISCSI_LOGIN_FLAG_USE_RAIDUS_VERIFICATION</p>
</td>
<td>
<p>Use RADIUS to verify CHAP response.  </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field AuthType

<dd>
<p>A <a href="storage.iscsi_auth_types">ISCSI_AUTH_TYPES</a> value that indicates the authentication method that is used to establish a logon connection. </p>
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
<dt>Iscsidef.h (include Iscsidef.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.iscsi_auth_types">ISCSI_AUTH_TYPES</a>
</dt>
<dt>
<a href="storage.iscsi_digest_types">ISCSI_DIGEST_TYPES</a>
</dt>
<dt>
<a href="storage.iscsi_loginoptions_wmi_class">ISCSI_LoginOptions WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_LoginOptions structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
