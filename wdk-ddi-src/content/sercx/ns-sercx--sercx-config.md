---
UID: NS.sercx._SERCX_CONFIG
title: SERCX_CONFIG
author: windows-driver-content
description: The SERCX_CONFIG structure contains configuration information for the serial framework extension (SerCx).
old-location: serports\sercx_config.htm
old-project: serports
ms.assetid: 2CBCBA07-C489-4475-A856-8748FBFDC141
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SERCX_CONFIG,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: sercx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SERCX_CONFIG
req.alt-loc: 1.0\Sercx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level.
req.iface: 
req.product: Windows 10 or later.
---

# SERCX_CONFIG structure



## -description
<p>The <b>SERCX_CONFIG</b> structure contains configuration information for the serial framework extension (SerCx).</p>


## -syntax

````
typedef struct _SERCX_CONFIG {
  ULONG                     Size;
  WDF_TRI_STATE             PowerManaged;
  PFN_SERCX_FILEOPEN        EvtSerCxFileOpen;
  PFN_SERCX_FILECLOSE       EvtSerCxFileClose;
  PFN_SERCX_FILECLEANUP     EvtSerCxFileCleanup;
  PFN_SERCX_TRANSMIT        EvtSerCxTransmit;
  PFN_SERCX_RECEIVE         EvtSerCxReceive;
  PFN_SERCX_WAITMASK        EvtSerCxWaitmask;
  PFN_SERCX_PURGE           EvtSerCxPurge;
  PFN_SERCX_CONTROL         EvtSerCxControl;
  PFN_SERCX_APPLY_CONFIG    EvtSerCxApplyConfig;
  PFN_SERCX_TRANSMIT_CANCEL EvtSerCxTransmitCancel;
  PFN_SERCX_RECEIVE_CANCEL  EvtSerCxReceiveCancel;
} SERCX_CONFIG, *PSERCX_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. The <a href="https://msdn.microsoft.com/library/windows/hardware/hh406711">SerCxInitialize</a> method uses this member to determine which version of the structure the caller is using. The size of this structure might change in future versions of the Sercx.h header file.</p>
</dd>

### -field <b>PowerManaged</b>

<dd>
<p>Whether the controller queue should be power-managed. If set to <b>WdfTrue</b>, the controller queue should be power-managed.  If set to <b>WdfFalse</b>, the controller queue not be power-managed. If set to <b>WdfDefault</b>, the controller queue should be power-managed unless the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547273">WdfFdoInitSetFilter</a> method. For more information, see the description of the <b>PowerManaged</b> member in <a href="https://msdn.microsoft.com/library/windows/hardware/ff552359">WDF_IO_QUEUE_CONFIG</a>.</p>
</dd>

### -field <b>EvtSerCxFileOpen</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-fileopen.md">EvtSerCxFileOpen</a> callback function. This member is optional and can be set to NULL.</p>
</dd>

### -field <b>EvtSerCxFileClose</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-fileclose.md">EvtSerCxFileClose</a> callback function. This member is optional and can be set to NULL.</p>
</dd>

### -field <b>EvtSerCxFileCleanup</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-filecleanup.md">EvtSerCxFileCleanup</a> callback function. This member is optional and can be set to NULL.</p>
</dd>

### -field <b>EvtSerCxTransmit</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-transmit.md">EvtSerCxTransmit</a> callback function. This member is required to point to a valid callback function.</p>
</dd>

### -field <b>EvtSerCxReceive</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-receive.md">EvtSerCxReceive</a> callback function. This member is required to point to a valid callback function.</p>
</dd>

### -field <b>EvtSerCxWaitmask</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-waitmask.md">EvtSerCxWaitmask</a> callback function. This member is required to point to a valid callback function.</p>
</dd>

### -field <b>EvtSerCxPurge</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-purge.md">EvtSerCxPurge</a> callback function. This member is optional and can be set to NULL.</p>
</dd>

### -field <b>EvtSerCxControl</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-control.md">EvtSerCxControl</a> callback function. This member is required to point to a valid callback function.</p>
</dd>

### -field <b>EvtSerCxApplyConfig</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-apply-config.md">EvtSerCxApplyConfig</a> callback function. This member is required to point to a valid callback function.</p>
</dd>

### -field <b>EvtSerCxTransmitCancel</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-transmit-cancel.md">EvtSerCxTransmitCancel</a> callback function. This member is optional and can be set to NULL.</p>
</dd>

### -field <b>EvtSerCxReceiveCancel</b>

<dd>
<p>A pointer to the controller driver's <a href="..\sercx\nc-sercx-evt-sercx-receive-cancel.md">EvtSerCxReceiveCancel</a> callback function. This member is optional and can be set to NULL.</p>
</dd>
</dl>

## -remarks
<p>Before this structure is passed to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406711">SerCxInitialize</a> method, it must be initialized by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439553">SERCX_CONFIG_INIT</a> function, and then modified by the controller driver to set the callback function pointers and the <b>PowerManaged</b> member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1.0\Sercx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-apply-config.md">EvtSerCxApplyConfig</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-control.md">EvtSerCxControl</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-filecleanup.md">EvtSerCxFileCleanup</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-fileclose.md">EvtSerCxFileClose</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-fileopen.md">EvtSerCxFileOpen</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-purge.md">EvtSerCxPurge</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-receive.md">EvtSerCxReceive</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-receive-cancel.md">EvtSerCxReceiveCancel</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-transmit.md">EvtSerCxTransmit</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-transmit-cancel.md">EvtSerCxTransmitCancel</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx-waitmask.md">EvtSerCxWaitmask</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439553">SERCX_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406711">SerCxInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547273">WdfFdoInitSetFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552359">WDF_IO_QUEUE_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20SERCX_CONFIG structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
