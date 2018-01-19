---
UID : NF:ufxclient.UfxEndpointNotifySetup
title : UfxEndpointNotifySetup function
author : windows-driver-content
description : Notifies UFX when the client driver receives a setup packet from the host.
old-location : buses\ufxendpointnotifysetup.htm
old-project : usbref
ms.assetid : 147CE46A-315D-4B75-B345-A7C0B01B2078
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : UfxEndpointNotifySetup
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ufxclient.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : UfxEndpointNotifySetup
req.alt-loc : ufxclient.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : DISPATCH_LEVEL
req.typenames : UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
req.product : Windows 10 or later.
---


# UfxEndpointNotifySetup function
Notifies UFX when the client driver receives a setup packet from the host.

## Syntax

````
VOID UfxEndpointNotifySetup(
  [in] UFXDEVICE                      UfxDevice,
  [in] PUSB_DEFAULT_PIPE_SETUP_PACKET SetupInfo
);
````

## Parameters

`UfxEndpoint`



`SetupInfo`

A pointer to a USB setup packet described in a <b>USB_DEFAULT_PIPE_SETUP_PACKET</b> structure (defined in Usbspec.h).


## Return Value

This method does not return a value.

## Remarks

The following example shows how to handle setup packet completion.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ufxclient.h |
| **Library** |  |
| **IRQL** | DISPATCH_LEVEL |
| **DDI compliance rules** |  |