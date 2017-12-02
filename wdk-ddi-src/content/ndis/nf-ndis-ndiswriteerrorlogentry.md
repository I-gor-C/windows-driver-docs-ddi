---
UID: NF.ndis.NdisWriteErrorLogEntry
title: NdisWriteErrorLogEntry
author: windows-driver-content
description: NdisWriteErrorLogEntry writes an entry to the system I/O error log file.
old-location: netvista\ndiswriteerrorlogentry.htm
old-project: netvista
ms.assetid: d36174ef-4df2-49ec-9167-cfb150f090f8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisWriteErrorLogEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisWriteErrorLogEntry (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisWriteErrorLogEntry (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWriteErrorLogEntry
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisWriteErrorLogEntry function



## -description
<p><b>NdisWriteErrorLogEntry</b> writes an entry to the system I/O error log file.</p>


## -syntax

````
VOID __cdecl NdisWriteErrorLogEntry(
  _In_ NDIS_HANDLE     NdisAdapterHandle,
  _In_ NDIS_ERROR_CODE ErrorCode,
  _In_ ULONG           NumberOfErrorValues,
                       ...
);
````


## -parameters
<dl>

### -param NdisAdapterHandle [in]

<dd>
<p>Specifies the handle representing the NIC that is the cause of the I/O error to be logged. This
     handle is an input parameter to 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>.</p>
</dd>

### -param ErrorCode [in]

<dd>
<p>Specifies the NDIS_ERRROR_CODE_<i>XXX</i> code that best describes the I/O error as one of the following values:
     </p>
<p></p>
<dl>

### -param NDIS_ERROR_CODE_RESOURCE_CONFLICT

<dd>
<p>The driver could not access a required resource.</p>
</dd>

### -param NDIS_ERROR_CODE_OUT_OF_RESOURCES

<dd>
<p>The hardware or driver ran out of resources.</p>
</dd>

### -param NDIS_ERROR_CODE_HARDWARE_FAILURE

<dd>
<p>The driver detected a hardware error.</p>
</dd>

### -param NDIS_ERROR_CODE_ADAPTER_NOT_FOUND

<dd>
<p>The network adapter was not found.</p>
</dd>

### -param NDIS_ERROR_CODE_INTERRUPT_CONNECT

<dd>
<p>The interrupt registration failed.</p>
</dd>

### -param NDIS_ERROR_CODE_DRIVER_FAILURE

<dd>
<p>A driver failure occurred that does not match any of the other error conditions.</p>
</dd>

### -param NDIS_ERROR_CODE_BAD_VERSION

<dd>
<p>The driver detected a version mismatch.</p>
</dd>

### -param NDIS_ERROR_CODE_TIMEOUT

<dd>
<p>A timeout expired.</p>
</dd>

### -param NDIS_ERROR_CODE_NETWORK_ADDRESS

<dd>
<p>A network address is invalid.</p>
</dd>

### -param NDIS_ERROR_CODE_UNSUPPORTED_CONFIGURATION

<dd>
<p>The requested driver configuration is not supported.</p>
</dd>

### -param NDIS_ERROR_CODE_INVALID_VALUE_FROM_ADAPTER

<dd>
<p>The network adapter hardware provided an invalid value.</p>
</dd>

### -param NDIS_ERROR_CODE_MISSING_CONFIGURATION_PARAMETER

<dd>
<p>A driver configuration parameter is missing in the registry.</p>
</dd>

### -param NDIS_ERROR_CODE_BAD_IO_BASE_ADDRESS

<dd>
<p>The I/O base address for the network adapter hardware is invalid.</p>
</dd>

### -param NDIS_ERROR_CODE_RECEIVE_SPACE_SMALL

<dd>
<p>The amount of receive buffer memory that is available is too small to receive data.</p>
</dd>

### -param NDIS_ERROR_CODE_ADAPTER_DISABLED

<dd>
<p>The network adapter hardware is disabled.</p>
</dd>
</dl>
</dd>

### -param NumberOfErrorValues [in]

<dd>
<p>Specifies the number of ULONG values to follow this parameter.</p>
</dd>

### -param ... 

<dd>
<p>Specifies a variable-sized array of ULONGs associated with the error to be logged.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisWriteErrorLogEntry</b> allocates an I/O error log record, fills in the record with the supplied
    information about the error, and then writes the record to the I/O error log file.</p>

<p>The system places a limit on the potential size of an error log record. For Windows 2000 and later
    versions, the limit is defined as ERROR_LOG_MAXIMUM_SIZE. The 
    <i>NumberOfErrorValues</i> passed to 
    <b>NdisWriteErrorLogEntry</b> therefore has a system-enforced limit, which is considerably less than the
    maximum possible value for a ULONG.</p>

<p>In practice, few callers of 
    <b>NdisWriteErrorLogEntry</b> even approach the limit for 
    <i>NumberOfErrorValues</i> because supplying many additional NDIS_STATUS_<i>XXX</i> values is not particularly helpful to the user or system administrator who later reads the
    error log, using the Win32 event viewer. Logging an I/O error at every possible opportunity is not
    particularly helpful to users either, so a miniport driver should log only critical I/O errors that can
    help a user or system administrator to debug a network failure for which the NIC is responsible on a
    particular machine or a configuration resource conflict discovered during driver initialization.</p>

<p>In general, a miniport driver calls 
    <b>NdisWriteErrorLogEntry</b> during initialization from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function if
    it cannot initialize a NIC that it controls or cannot allocate the hardware resources it needs to carry
    out I/O operations on a NIC. A miniport driver also can call 
    <b>NdisWriteErrorLogEntry</b> when a device-reset operation fails due to unrecoverable hardware error(s).
    Logging these kinds of I/O errors helps users or system administrators to identify a badly configured NIC
    or a NIC with failing hardware components.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/c9306c1b-b97f-4b32-9780-c903c48edeb8">NdisWriteErrorLogEntry (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisWriteErrorLogEntry (NDIS
   5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisWriteErrorLogEntry function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
