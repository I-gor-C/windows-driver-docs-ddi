---
UID: NN:wia_lh.IWiaLog
title: IWiaLog
author: windows-driver-content
description: The IWiaLog interface provides methods to enable minidrivers to log trace, error, and warning messages to the diagnostic log file Wiaservc.log.
old-location: image\iwialog_interface.htm
old-project: Image
ms.assetid: b56cb3f0-1053-4104-b223-e7448a832f33
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: image.iwialog_interface, IWiaLog interface [Imaging Devices], IWiaLog interface [Imaging Devices], described, IWiaLog, wia_lh/IWiaLog, IWiaLog_0284e394-6bc5-40b8-8174-0041bfc0d5dd.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wia_lh.h
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
req.lib: wia_lh.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	wia_lh.h
apiname:
-	IWiaLog
product: Windows
targetos: Windows
req.typenames: "*PBMP_IMAGE_INFO, BMP_IMAGE_INFO"
req.product: Windows 10 or later.
---

# IWiaLog interface

<div class="alert"><b>Note</b>  <p class="note">The IWiaLog interface is obsolete for Microsoft Windows XP and later and is no longer supported. Instead, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540599">Diagnostic Log Macros</a>.

</div><div> </div>
The <b>IWiaLog</b> interface provides methods to enable minidrivers to log trace, error, and warning messages to the diagnostic log file Wiaservc.log. The prototypes for the methods appear in Wia.h. The diagnostic log file Wiaservc.log is found in the Windows directory, or in the directory returned by the GetWindowsDirectory system API call, which is described in the Microsoft Windows SDK documentation.

## Methods

<p>The <b>IWiaLog</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wia_lh.IWiaLog.hResult](nf-wia_lh-iwialog-hresult.md) | Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported. |
| [wia_lh.IWiaLog.InitializeLog](nf-wia_lh-iwialog-initializelog.md) | Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.The IWiaLog::InitializeLog method initializes the lWiaLog interface. |
| [wia_lh.IWiaLog.Log](nf-wia_lh-iwialog-log.md) | The IWiaLog interface is obsolete for Windows XP and later, and is no longer supported. Use the Diagnostic Log Macros instead.The IWiaLog::Log method writes a diagnostic log message to Wiaservc.log. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wia_lh.h |