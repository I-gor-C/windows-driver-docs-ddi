---
UID : NN:wudfddi.IWDFRemoteTarget
title : IWDFRemoteTarget
author : windows-driver-content
description : To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2::CreateRemoteTarget.
old-location : wdf\iwdfremotetarget.htm
old-project : wdf
ms.assetid : 60164136-4d4b-4e42-8504-ddd907edf0e9
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfremotetarget, IWDFRemoteTarget interface, IWDFRemoteTarget interface, described, IWDFRemoteTarget, wudfddi/IWDFRemoteTarget, UMDFIoTargetObjectRef_5b14493b-370a-40a0-b571-dbd03b2a19a0.xml, umdf.iwdfremotetarget
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.9
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
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

# IWDFRemoteTarget interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFRemoteTarget</b> interface, drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff556928">IWDFDevice2::CreateRemoteTarget</a>.

## Methods

<p>The <b>IWDFRemoteTarget</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFRemoteTarget.Close](nf-wudfddi-iwdfremotetarget-close.md) | The Close method closes a remote I/O target. |
| [wudfddi.IWDFRemoteTarget.CloseForQueryRemove](nf-wudfddi-iwdfremotetarget-closeforqueryremove.md) | The CloseForQueryRemove method closes a remote I/O target because the operating system might allow the device to be removed. |
| [wudfddi.IWDFRemoteTarget.GetState](nf-wudfddi-iwdfremotetarget-getstate.md) | The GetState method returns the current state of a remote I/O target. |
| [wudfddi.IWDFRemoteTarget.OpenFileByName](nf-wudfddi-iwdfremotetarget-openfilebyname.md) | The OpenFileByName method opens a remote I/O target that is a file. |
| [wudfddi.IWDFRemoteTarget.OpenRemoteInterface](nf-wudfddi-iwdfremotetarget-openremoteinterface.md) | The OpenRemoteInterface method opens a device interface so that the driver can send I/O requests to it. |
| [wudfddi.IWDFRemoteTarget.Reopen](nf-wudfddi-iwdfremotetarget-reopen.md) | The Reopen method reopens a remote I/O target after it has been temporarily closed. |
| [wudfddi.IWDFRemoteTarget.Start](nf-wudfddi-iwdfremotetarget-start.md) | The IWDFRemoteTarget::Start method restarts a remote I/O target that is stopped. |
| [wudfddi.IWDFRemoteTarget.Stop](nf-wudfddi-iwdfremotetarget-stop.md) | The Stop method temporarily stops a remote I/O target. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |