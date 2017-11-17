---
UID: NS.iscsiop._RemovePersistentLogin_IN
title: RemovePersistentLogin_IN
author: windows-driver-content
description: The RemovePersistentLogin_IN structure holds the input data for the RemovePersistentLogin method, which is used to remove persistent login information.
old-location: storage\removepersistentlogin_in.htm
ms.assetid: 94dc7a87-83a0-419d-914c-008d797fec87
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
req.alt-api: RemovePersistentLogin_IN
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
ms.keywords: RemovePersistentLogin_IN, RemovePersistentLogin_IN, *PRemovePersistentLogin_IN
req.iface: 
---

# RemovePersistentLogin_IN structure



## -description
<p>The RemovePersistentLogin_IN structure holds the input data for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563995">RemovePersistentLogin</a> method, which is used to remove persistent login information.</p>


## -syntax

````
typedef struct _RemovePersistentLogin_IN {
  ULONG              PortNumber;
  WCHAR              TargetName[223 + 1];
  ISCSI_TargetPortal TargetPortal;
} RemovePersistentLogin_IN, *PRemovePersistentLogin_IN;
````


## -struct-fields
<dl>

### -field <b>PortNumber</b>

<dd>
<p>The port number from which the initiator established the logon session.</p>
</dd>

### -field <b>TargetName</b>

<dd>
<p>The iSCSI target name to be removed from the initiator's list of persistent logon targets.</p>
</dd>

### -field <b>TargetPortal</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a> structure that specifies the target portal for which the initiator should delete persistent logons. ISCSI_TargetPortal has an <b>Address</b> member of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff561536">ISCSI_IP_Address</a>. If the <b>Type</b> member of ISCSI_IP_Address is set to ISCSI_IP_ADDRESS_EMPTY, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563995">RemovePersistentLogin</a> method removes the persistent logons to the target for all portals.</p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561536">ISCSI_IP_Address</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561574">ISCSI_TargetPortal</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563995">RemovePersistentLogin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564008">RemovePersistentLogin_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20RemovePersistentLogin_IN structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
