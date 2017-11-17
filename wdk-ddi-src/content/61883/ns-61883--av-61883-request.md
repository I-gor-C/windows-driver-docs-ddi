---
UID: NS.61883._AV_61883_REQUEST
title: AV_61883_REQUEST
author: windows-driver-content
description: The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver.
old-location: ieee\av_61883_request.htm
ms.assetid: 697fbf86-5c99-4e35-bcb4-a6f5272cc987
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 61883.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AV_61883_REQUEST
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
ms.keywords: AV_61883_REQUEST, AV_61883_REQUEST, *PAV_61883_REQUEST
---

# AV_61883_REQUEST structure



## -description
<p>The AV_61883_REQUEST structure is used to pass requests to the IEC-61883 protocol driver.</p>


## -syntax

````
typedef struct _AV_61883_REQUEST {
  ULONG Function;
  ULONG Version;
  ULONG Flags;
  union {
    GET_UNIT_INFO       GetUnitInfo;
    SET_UNIT_INFO       SetUnitInfo;
    CMP_GET_PLUG_HANDLE GetPlugHandle;
    CMP_GET_PLUG_STATE  GetPlugState;
    CMP_CONNECT         Connect;
    CMP_DISCONNECT      Disconnect;
    CIP_ATTACH_FRAME    AttachFrame;
    CIP_CANCEL_FRAME    CancelFrame;
    CIP_TALK            Talk;
    CIP_LISTEN          Listen;
    CIP_STOP            Stop;
    FCP_REQUEST         Request;
    FCP_RESPONSE        Response;
    FCP_SEND_REQUEST    SendRequest;
    FCP_GET_RESPONSE    GetResponse;
    FCP_GET_REQUEST     GetRequest;
    FCP_SEND_RESPONSE   SendResponse;
    SET_FCP_NOTIFY      SetFcpNotify;
    CMP_CREATE_PLUG     CreatePlug;
    CMP_DELETE_PLUG     DeletePlug;
    CMP_SET_PLUG        SetPlug;
    BUS_RESET_NOTIFY    BusResetNotify;
    SET_UNIT_DIRECTORY  SetUnitDirectory;
    CMP_MONITOR_PLUGS   MonitorPlugs;
  };
} AV_61883_REQUEST, *PAV_61883_REQUEST;
````


## -struct-fields
<dl>

### -field <b>Function</b>

<dd>
<p>Determines the type of request. Each request type is documented under the value of <b>Function</b> in <a href="https://msdn.microsoft.com/library/windows/hardware/ff537195">IEC-61883 Protocol I/O Requests</a>.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The device driver interface (DDI) version for the request. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff537219">INIT_61883_HEADER</a> macro initializes <b>Version</b> to CURRENT_61883_DDI_VERSION.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags specific to the request. For details, see the reference page for the request. Drivers must set this member to zero for requests that do not use flags.</p>
</dd>

### -field <b>GetUnitInfo</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/2FE13A53-5B88-40B8-B129-8DD141F1B160">GET_UNIT_INFO</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536983">Av61883_GetUnitInfo</a>.</p>
</dd>

### -field <b>SetUnitInfo</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/D4A9B507-E199-42EA-BC29-6F477BEC8D20">SET_UNIT_INFO</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff537002">Av61883_SetUnitInfo</a>.</p>
</dd>

### -field <b>GetPlugHandle</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/4EDEE2EE-7B42-4CC9-8CFC-4690193C5D4D">CMP_GET_PLUG_HANDLE</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536979">Av61883_GetPlugHandle</a>.</p>
</dd>

### -field <b>GetPlugState</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/76BC179A-7484-433C-8467-B13BA7008B90">CMP_GET_PLUG_STATE</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536980">Av61883_GetPlugState</a>.</p>
</dd>

### -field <b>Connect</b>

<dd>
<p>A CMP_CONNECT structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536958">Av61883_Connect</a>.</p>
</dd>

### -field <b>Disconnect</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/7EAE617D-EFF9-4F77-9B9C-5985B864B310">CMP_DISCONNECT</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536966">Av61883_Disconnect</a>.</p>
</dd>

### -field <b>AttachFrame</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/F7E283BB-B714-4CD4-AFF4-EFB62D82791D">CIP_ATTACH_FRAME</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536950">Av61883_AttachFrame</a>.</p>
</dd>

### -field <b>CancelFrame</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/952625D0-BA82-40C1-8EBF-8CD54C0E4C40">CIP_CANCEL_FRAME</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536956">Av61883_CancelFrame</a>.</p>
</dd>

### -field <b>Talk</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/DD5EB79D-122B-4D17-9109-37473AC49C4A">CIP_TALK</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff537007">Av61883_Talk</a>.</p>
</dd>

### -field <b>Listen</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/362ABECF-66D3-4B0B-913B-59F7196D6BFD">CIP_LISTEN</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536985">Av61883_Listen</a>.</p>
</dd>

### -field <b>Stop</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/FE396C2C-B099-47F4-9C27-93D420D54103">CIP_STOP</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff537005">Av61883_Stop</a>.</p>
</dd>

### -field <b>Request</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/82F36729-57E0-49AB-8C2D-BCBA6EED33EE">FCP_SEND_REQUEST</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536992">Av61883_SendFcpResponse</a>.</p>
</dd>

### -field <b>Response</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/1CE962A4-7F99-4F81-8B85-265A4225B88A">FCP_GET_RESPONSE</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536977">Av61883_GetFcpResponse</a>.</p>
</dd>

### -field <b>SendRequest</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/82F36729-57E0-49AB-8C2D-BCBA6EED33EE">FCP_SEND_REQUEST</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536992">Av61883_SendFcpResponse</a>.</p>
</dd>

### -field <b>GetResponse</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/1CE962A4-7F99-4F81-8B85-265A4225B88A">FCP_GET_RESPONSE</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536977">Av61883_GetFcpResponse</a>.</p>
</dd>

### -field <b>GetRequest</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/4DD05230-E9CA-4067-984B-7F0540FE8079">FCP_GET_REQUEST</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536974">Av61883_GetFcpRequest</a>.</p>
</dd>

### -field <b>SendResponse</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/65C76CA1-F7F2-4DFD-B928-0595A137BF28">FCP_SEND_RESPONSE</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536992">Av61883_SendFcpResponse</a>.</p>
</dd>

### -field <b>SetFcpNotify</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/94A966C4-9FFA-4937-B7D8-D1A3608E4A7F">SET_FCP_NOTIFY</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536993">Av61883_SetFcpNotify</a>.</p>
</dd>

### -field <b>CreatePlug</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/4FE3FE9E-9F00-431D-99F0-002B1368CE34">CMP_CREATE_PLUG</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536961">Av61883_CreatePlug</a>.</p>
</dd>

### -field <b>DeletePlug</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/93F81B97-5C37-47BF-8867-0FBEFA8F6D3B">CMP_DELETE_PLUG</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536964">Av61883_DeletePlug</a>.</p>
</dd>

### -field <b>SetPlug</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/2C47165D-9D04-46C8-A1EC-04E6F32AE516">CMP_SET_PLUG</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536995">Av61883_SetPlug</a>.</p>
</dd>

### -field <b>BusResetNotify</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/9CF14B12-D94F-486D-A5FC-E7CC2730D8E9">BUS_RESET_NOTIFY</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536955">Av61883_BusResetNotify</a>.</p>
</dd>

### -field <b>SetUnitDirectory</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/C4021856-835D-4B4B-9795-4FEEEFAC06B8">SET_UNIT_DIRECTORY</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536998">Av61883_SetUnitDirectory</a>.</p>
</dd>

### -field <b>MonitorPlugs</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/D281BCBB-CDC6-442C-9A47-DF07D1BE1B28">CMP_MONITOR_PLUGS</a> structure, used if the <b>Function</b> member is <a href="https://msdn.microsoft.com/library/windows/hardware/ff536987">Av61883_MonitorPlugs</a>.</p>
</dd>
</dl>

## -remarks
<p>The <b>Parameters-&gt;</b><b>Others.Arguments1</b> member of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537234">IOCTL_61883_CLASS</a> IRP points to an AV_61883_REQUEST structure. The IEC-61883 protocol driver uses the request structure to determine the type of request made by the client driver, and also to return the results of the operation. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537195">IEC-61883 Protocol I/O Requests</a> for a description of the behavior of each request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>61883.h (include 61883.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537219">INIT_61883_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537234">IOCTL_61883_CLASS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20AV_61883_REQUEST structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
