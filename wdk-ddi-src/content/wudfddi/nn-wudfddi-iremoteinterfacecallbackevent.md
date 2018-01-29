---
UID : NN:wudfddi.IRemoteInterfaceCallbackEvent
title : IRemoteInterfaceCallbackEvent
author : windows-driver-content
description : The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface.
old-location : wdf\iremoteinterfacecallbackevent.htm
old-project : wdf
ms.assetid : 72b68ed0-d14c-44b1-b848-40c427fe6c9a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iremoteinterfacecallbackevent, IRemoteInterfaceCallbackEvent interface, IRemoteInterfaceCallbackEvent interface, described, IRemoteInterfaceCallbackEvent, wudfddi/IRemoteInterfaceCallbackEvent, UMDFIoTargetObjectRef_9ce0aebc-e132-4d0e-b575-7ef1e19d9c30.xml, umdf.iremoteinterfacecallbackevent
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IRemoteInterfaceCallbackEvent interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IRemoteInterfaceCallbackEvent</b> interface provides a callback function that the framework calls to notify the driver about device events that are associated with a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-interfaces-in-umdf-drivers">device interface</a>.

## Methods

<p>The <b>IRemoteInterfaceCallbackEvent</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IRemoteInterfaceCallbackEvent.OnRemoteInterfaceEvent](nf-wudfddi-iremoteinterfacecallbackevent-onremoteinterfaceevent.md) | A UMDF-based driver's OnRemoteInterfaceEvent event callback function handles device events that are associated with a device interface. |

## Remarks

If your driver supports an <b>IRemoteInterfaceCallbackEvent</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a> must return the interface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |