---
UID : NN:wudfddi.IPnpCallback
title : IPnpCallback
author : windows-driver-content
description : The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface.
old-location : wdf\ipnpcallback.htm
old-project : wdf
ms.assetid : b6ab28e1-08d5-49ee-931a-8e2fe68bd75e
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.ipnpcallback, IPnpCallback interface, IPnpCallback interface, described, IPnpCallback, wudfddi/IPnpCallback, UMDFDeviceObjectRef_1e101e13-802b-4196-a76c-ed4103d6fbe3.xml, umdf.ipnpcallback
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : Wudfddi.h
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
req.typenames : POWER_ACTION, *PPOWER_ACTION
req.product : Windows 10 or later.
---

# IPnpCallback interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IPnpCallback</b> interface is a Plug and Play (PnP) and power management (PM) interface.

## Methods

<p>The <b>IPnpCallback</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IPnpCallback.OnD0Entry](nf-wudfddi-ipnpcallback-ond0entry.md) | The OnD0Entry method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. |
| [wudfddi.IPnpCallback.OnD0Exit](nf-wudfddi-ipnpcallback-ond0exit.md) | The OnD0Exit method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations, such as disabling the device. |
| [wudfddi.IPnpCallback.OnQueryRemove](nf-wudfddi-ipnpcallback-onqueryremove.md) | The OnQueryRemove method notifies a driver before a device is removed from a computer. |
| [wudfddi.IPnpCallback.OnQueryStop](nf-wudfddi-ipnpcallback-onquerystop.md) | The OnQueryStop method notifies a driver before a device is stopped. |
| [wudfddi.IPnpCallback.OnSurpriseRemoval](nf-wudfddi-ipnpcallback-onsurpriseremoval.md) | The OnSurpriseRemoval method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations. |

## Remarks

A driver registers the <b>IPnpCallback</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h (include Wudfddi.h) |