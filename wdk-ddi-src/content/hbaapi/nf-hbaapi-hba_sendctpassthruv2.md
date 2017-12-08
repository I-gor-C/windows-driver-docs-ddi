---
UID: NF.hbaapi.HBA_SendCTPassThruV2
title: HBA_SendCTPassThruV2 function
author: windows-driver-content
description: The HBA_SendCTPassThruV2 routine sends a common transport (CT) pass-through command through the indicated port.
old-location: storage\hba_sendctpassthruv2.htm
old-project: storage
ms.assetid: 95526c2d-19bf-4f4a-abfa-e5be73c1a6a5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_SendCTPassThruV2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_SendCTPassThruV2
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
---

# HBA_SendCTPassThruV2 function



## -description
The <b>HBA_SendCTPassThruV2</b> routine sends a common transport (CT) pass-through command through the indicated port. 


## -syntax

````
HBA_STATUS HBA_API HBA_SendCTPassThruV2(
  _In_    HBA_HANDLE HbaHandle,
  _In_    HBA_WWN    HbaPortWWN,
  _In_    void       *pReqBuffer,
  _In_    HBA_UINT32 ReqBufferSize,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *RspBufferSize
);
````


## -parameters

### -param HbaHandle [in]

Contains a value returned by the routine <a href="storage.hba_openadapter">HBA_OpenAdapter</a> that identifies the HBA that will route the CT command. The HBA routes the CT command to the server that runs the service requested by the CT command. 

### -param HbaPortWWN [in]

Contains the worldwide name (WWN) of the port from which to issue the command. For a definition of worldwide names, see the T11 committee's specification for <i>Fibre Channel HBA API</i>. 

### -param pReqBuffer [in]

Pointer to a buffer that contains the full frame of the common transport command in big-endian format.

### -param ReqBufferSize [in]

Indicates the size of the buffer pointed to by <i>pReqBuffer</i>:

### -param pRspBuffer [out]

Pointer to a buffer that contains the payload data from the reply to the common transport command in big-endian (wire) format. 

### -param RspBufferSize [in, out]

On input, indicates the size, in bytes, of the buffer pointed to by <i>pRspBuffer</i>. On return, this member indicates the size, in bytes, of the response data. 

## -returns
The <b>HBA_SendCTPassThruV2</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. If the HBA successfully delivers the command to the destination service, and the service executes the command and successfully returns the results, the HBA_SendCTPassThru routine returns a value of HBA_STATUS_OK. If the command does not succeed, this routine returns an appropriate error code of type HBA_STATUS.

## -remarks
The <b>HBA_SendCTPassThruV2</b> library routine is identical to the <a href="storage.hba_sendctpassthru">HBA_SendCTPassThru</a> routine, except that <b>HBA_SendCTPassThruV2</b> allows the caller to specify the port through which the CT command will be issued. 

The <b>HBA_SendCTPassThruV2</b> library routine serves a purpose very similar to the <a href="storage.sendctpassthru">SendCTPassThru</a> WMI method. 

A CT command can request services that distribute encryption keys, IP addresses, time stamps, names, aliases, fabric configuration, and security policies. For a complete list of the service types that can be specified in a CT command, see the <i>Fibre Channel Generic Services - 4 (FC-GS-4)</i> specification published by the ANSI committee. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hba_openadapter">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="storage.hba_sendctpassthru">HBA_SendCTPassThru</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
<dt>
<a href="storage.sendctpassthru">SendCTPassThru</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_SendCTPassThruV2 routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
