---
UID: NS.iscsifnd._ISCSI_DiscoveredTarget2
title: ISCSI_DiscoveredTarget2
author: windows-driver-content
description: The ISCSI_DiscoveredTarget2 structure contains information that is related to a discovered target device.
old-location: storage\iscsi_discoveredtarget2.htm
old-project: storage
ms.assetid: 77fb2942-5836-44cb-9a5e-e45f6a022264
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ISCSI_DiscoveredTarget2, ISCSI_DiscoveredTarget2, *PISCSI_DiscoveredTarget2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsifnd.h
req.include-header: Iscsifnd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_DiscoveredTarget2
req.alt-loc: iscsifnd.h
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

# ISCSI_DiscoveredTarget2 structure



## -description
<p>The ISCSI_DiscoveredTarget2 structure contains information that is related to a discovered target device. </p>


## -syntax

````
typedef struct _ISCSI_DiscoveredTarget2 {
  ULONG                              TargetPortalGroupCount;
  WCHAR                              TargetName[223 + 1];
  WCHAR                              TargetAlias[255 + 1];
  ISCSI_DiscoveredTargetPortalGroup2 TargetDiscoveredPortalGroups[1];
} ISCSI_DiscoveredTarget2, *PISCSI_DiscoveredTarget2;
````


## -struct-fields
<dl>

### -field TargetPortalGroupCount

<dd>
<p>The number of portal groups that are associated with the target.</p>
</dd>

### -field TargetName

<dd>
<p>A name for the target that uniquely identifies the target anywhere in the world. For more information about how to specify this name, see the <i>iSCSI </i>specification that is published by the Internet Engineering Task Force (IETF) of the IP storage working group. </p>
</dd>

### -field TargetAlias

<dd>
<p>The human-readable name or description that is assigned to the target device by its host operating system. You can use this name in user interfaces, but it is not unique, so you should not use it in authentication decisions. </p>
</dd>

### -field TargetDiscoveredPortalGroups

<dd>
<p>A variable-length array of <a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtargetportalgroup2.md">ISCSI_DiscoveredTargetPortalGroup2</a> structures that contains information about the portal groups that the initiator can use to connect to the target.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite automatically generates a declaration of the ISCSI_DiscoveredTarget2 structure when it compiles the <a href="storage.iscsi_discoveredtarget2_wmi_class">ISCSI_DiscoveredTarget2 WMI Class</a> in <i>Discover.mof</i>.</p>

<p>The only difference between the ISCSI_DiscoveredTarget2 structure and the <a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtarget.md">ISCSI_DiscoveredTarget</a> structure is that the <b>TargetDiscoveredPortalGroups</b> member of ISCSI_DiscoveredTarget2 is a <a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtargetportalgroup2.md">ISCSI_DiscoveredTargetPortalGroup2</a> structure instead of a <a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtargetportalgroup.md">ISCSI_DiscoveredTargetPortalGroup</a> structure.  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsifnd.h (include Iscsifnd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtarget.md">ISCSI_DiscoveredTarget</a>
</dt>
<dt>
<a href="storage.iscsi_discoveredtarget_wmi_class">ISCSI_DiscoveredTarget WMI Class</a>
</dt>
<dt>
<a href="storage.iscsi_discoveredtarget2_wmi_class">ISCSI_DiscoveredTarget2 WMI Class</a>
</dt>
<dt>
<a href="..\iscsifnd\ns-iscsifnd--iscsi-discoveredtargetportalgroup.md">ISCSI_DiscoveredTargetPortalGroup</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ISCSI_DiscoveredTarget2 structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
