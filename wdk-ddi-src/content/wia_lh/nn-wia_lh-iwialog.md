---
UID : NN:wia_lh.IWiaLog
title : IWiaLog
author : windows-driver-content
description : The IWiaLog interface provides methods to enable minidrivers to log trace, error, and warning messages to the diagnostic log file Wiaservc.log.
old-location : image\iwialog_interface.htm
old-project : image
ms.assetid : b56cb3f0-1053-4104-b223-e7448a832f33
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : IWiaTransferCallback, IWiaTransferCallback::TransferCallback, TransferCallback
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wia_lh.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IWiaLog
req.alt-loc : wia_lh.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : BMP_IMAGE_INFO, *PBMP_IMAGE_INFO
req.product : Windows 10 or later.
---

# IWiaLog interface



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
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wia_lh.h |
| **DLL** |  |