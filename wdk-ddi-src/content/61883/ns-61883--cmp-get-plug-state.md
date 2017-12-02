---
UID: NS.61883._CMP_GET_PLUG_STATE
title: CMP_GET_PLUG_STATE
author: windows-driver-content
description: This structure is used in getting the state of a plug.
old-location: ieee\cmp_get_plug_state.htm
old-project: IEEE
ms.assetid: 76BC179A-7484-433C-8467-B13BA7008B90
ms.author: windowsdriverdev
ms.date: 11/29/2017
ms.keywords: CMP_GET_PLUG_STATE, CMP_GET_PLUG_STATE, *PCMP_GET_PLUG_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CMP_GET_PLUG_STATE
req.alt-loc: 61883.h
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

# CMP_GET_PLUG_STATE structure



## -description
<p>This structure is used in getting the state of a plug.The  request retrieves state information for the specified plug, including its current connections and bus data format. Plug state is volatile and can change unexpectedly. </p>


## -syntax

````
typedef struct _CMP_GET_PLUG_STATE {
  HANDLE hPlug;
  ULONG  State;
  ULONG  DataRate;
  ULONG  Payload;
  ULONG  BC_Connections;
  ULONG  PP_Connections;
} CMP_GET_PLUG_STATE, *PCMP_GET_PLUG_STATE;
````


## -struct-fields
<dl>

### -field hPlug

<dd>
<p>On input, the handle of the plug to retrieve state information.</p>
</dd>

### -field State

<dd>
<p>On output, the state of the plug. Can be one of the following:</p>
<p>CMP_PLUG_STATE_IDLE </p>
<p>CMP_PLUG_STATE_READY </p>
<p>CMP_PLUG_STATE_SUSPENDED </p>
<p>CMP_PLUG_STATE_ACTIVE </p>
</dd>

### -field DataRate

<dd>
<p>On output, the data rate of the plug. Can be one of the following: </p>
<p>CMP_SPEED_S100 </p>
<p>CMP_SPEED_S200 </p>
<p>CMP_SPEED_S400 </p>
</dd>

### -field Payload

<dd>
<p>On output, the payload size for the plug.</p>
</dd>

### -field BC_Connections

<dd>
<p>On output, the number of broadcast connections associated with the plug.</p>
</dd>

### -field PP_Connections

<dd>
<p>On output, the number of point-to-point connections associated with the plug.</p>
</dd>
</dl>

## -remarks
<p>If successful, the IEC-61883 protocol driver sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_SUCCESS. </p>

<p>If an incorrect parameter is passed in, the protocol driver sets <b>Irp-&gt;IoStatus.Status </b>to STATUS_INVALID_PARAMETER.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20CMP_GET_PLUG_STATE structure%20 RELEASE:%20(11/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
