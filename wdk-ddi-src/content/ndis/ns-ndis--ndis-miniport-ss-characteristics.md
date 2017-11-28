---
UID: NS.ndis._NDIS_MINIPORT_SS_CHARACTERISTICS
title: NDIS_MINIPORT_SS_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_MINIPORT_SS_CHARACTERISTICS structure specifies the pointers to a miniport driver's NDIS selective suspend handler functions. These functions are called by NDIS to issue idle notifications to the driver during a selective suspend operation.
old-location: netvista\ndis_miniport_ss_characteristics.htm
old-project: netvista
ms.assetid: 325E5717-6B84-45AE-85D4-BA1839DB76A2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_MINIPORT_SS_CHARACTERISTICS, NDIS_MINIPORT_SS_CHARACTERISTICS, *PNDIS_MINIPORT_SS_CHARACTERISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_SS_CHARACTERISTICS
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_MINIPORT_SS_CHARACTERISTICS structure



## -description
<p>
<p>The <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure specifies the pointers to a miniport driver's NDIS selective suspend handler functions. These functions are called by NDIS to issue idle notifications to the driver during a selective suspend operation.</p>
</p>
<p>The <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure specifies the pointers to a miniport driver's NDIS selective suspend handler functions. These functions are called by NDIS to issue idle notifications to the driver during a selective suspend operation.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_SS_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                        Header;
  ULONG                                     Flags;
  MINIPORT_IDLE_NOTIFICATION_HANDLER        IdleNotificationHandler;
  MINIPORT_CANCEL_IDLE_NOTIFICATION_HANDLER CancelIdleNotificationHandler;
} NDIS_MINIPORT_SS_CHARACTERISTICS, *PNDIS_MINIPORT_SS_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_MINIPORT_SS_CHARACTERISTICS. To specify the version of the <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_SS_CHARACTERISTICS_REVISION_1"></a><a id="ndis_miniport_ss_characteristics_revision_1"></a>NDIS_MINIPORT_SS_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_MINIPORT_SS_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p> A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>IdleNotificationHandler</b>

<dd>
<p>A pointer to the miniport driver's <a href="..\ndis\nc-ndis-miniport-idle-notification.md">MiniportIdleNotification</a> function.</p>
</dd>

### -field <b>CancelIdleNotificationHandler</b>

<dd>
<p>A pointer to the miniport driver's <a href="..\ndis\nc-ndis-miniport-cancel-idle-notification.md">MiniportCancelIdleNotification</a> function.</p>
</dd>
</dl>

## -remarks
<p>To register the handler functions for NDIS selective suspend, the miniport driver follows these steps when its <a href="netvista.miniportsetoptions">MiniportSetOptions</a> function is called:</p>

<p>The miniport driver initializes an <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure with pointers to the handler functions.</p>

<p>The miniport driver  then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> and sets the <i>OptionalHandlers</i> parameter to a pointer to the <b>NDIS_MINIPORT_SS_CHARACTERISTICS</b> structure.</p>

<p>For more information on how to handle idle notifications for NDIS selective suspend, see <a href="NULL">NDIS Selective Suspend Idle Notifications</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-cancel-idle-notification.md">MiniportCancelIdleNotification</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-idle-notification.md">MiniportIdleNotification</a>
</dt>
<dt>
<a href="netvista.miniportsetoptions">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_SS_CHARACTERISTICS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
