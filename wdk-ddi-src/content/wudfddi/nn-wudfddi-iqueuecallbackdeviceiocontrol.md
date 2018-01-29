---
UID : NN:wudfddi.IQueueCallbackDeviceIoControl
title : IQueueCallbackDeviceIoControl
author : windows-driver-content
description : An I/O queue object notifies a driver when a device I/O control request is available for the driver.
old-location : wdf\iqueuecallbackdeviceiocontrol.htm
old-project : wdf
ms.assetid : efb33bc5-2a9b-40c7-9584-c762daf016f6
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iqueuecallbackdeviceiocontrol, IQueueCallbackDeviceIoControl interface, IQueueCallbackDeviceIoControl interface, described, IQueueCallbackDeviceIoControl, wudfddi/IQueueCallbackDeviceIoControl, UMDFQueueObjectRef_43ec96af-39ec-4d9c-89bd-c8d08bec3999.xml, umdf.iqueuecallbackdeviceiocontrol
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

# IQueueCallbackDeviceIoControl interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

An I/O queue object notifies a driver when a device I/O control request is available for the driver. The I/O queue object notifies the driver in response to an application calling the Microsoft Win32 <b>DeviceIoControl</b> function. The driver can handle the notification by registering the <b>IQueueCallbackDeviceIoControl</b> interface.

## Methods

<p>The <b>IQueueCallbackDeviceIoControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IQueueCallbackDeviceIoControl.OnDeviceIoControl](nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol.md) | The OnDeviceIoControl method is called to handle a device I/O control request when an application performs a specific operation on a device through the Microsoft Win32 OnDeviceIoControl function. |

## Remarks

A driver registers the <b>IQueueCallbackDeviceIoControl</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. For more information about creating or configuring an I/O queue, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/configuring-dispatch-mode-for-an-i-o-queue">Configuring Dispatch Mode for an I/O Queue</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |