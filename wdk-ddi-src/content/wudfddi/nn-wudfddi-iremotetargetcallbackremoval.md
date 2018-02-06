---
UID: NN:wudfddi.IRemoteTargetCallbackRemoval
title: IRemoteTargetCallbackRemoval
author: windows-driver-content
description: The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target.
old-location: wdf\iremotetargetcallbackremoval.htm
old-project: wdf
ms.assetid: 72271173-8851-4980-9b52-f9e14f1fe071
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iremotetargetcallbackremoval, IRemoteTargetCallbackRemoval interface, IRemoteTargetCallbackRemoval interface, described, IRemoteTargetCallbackRemoval, wudfddi/IRemoteTargetCallbackRemoval, UMDFIoTargetObjectRef_7508512a-9bfc-4563-bf01-48e9caf6ba4f.xml, umdf.iremotetargetcallbackremoval
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	wudfddi.h
apiname:
-	IRemoteTargetCallbackRemoval
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IRemoteTargetCallbackRemoval interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IRemoteTargetCallbackRemoval</b> interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/general-i-o-targets-in-umdf">remote I/O target</a>.

## Methods

<p>The <b>IRemoteTargetCallbackRemoval</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IRemoteTargetCallbackRemoval.OnRemoteTargetQueryRemove](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetqueryremove.md) | A UMDF-based driver's OnRemoteTargetQueryRemove event callback function determines whether a remote I/O target's device can be stopped and removed. |
| [wudfddi.IRemoteTargetCallbackRemoval.OnRemoteTargetRemoveCanceled](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecanceled.md) | A UMDF-based driver's OnRemoteTargetRemoveCanceled event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device. |
| [wudfddi.IRemoteTargetCallbackRemoval.OnRemoteTargetRemoveComplete](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecomplete.md) | A UMDF-based driver's OnRemoteTargetRemoveComplete event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device. |

## Remarks

If your driver supports an <b>IRemoteTargetCallbackRemoval</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff556928">IWDFDevice2::CreateRemoteTarget</a> must return the interface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h |