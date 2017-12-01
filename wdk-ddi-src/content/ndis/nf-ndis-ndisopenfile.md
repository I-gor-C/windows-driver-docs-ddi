---
UID: NF.ndis.NdisOpenFile
title: NdisOpenFile
author: windows-driver-content
description: The NdisOpenFile function returns a handle for an opened file.
old-location: netvista\ndisopenfile.htm
old-project: netvista
ms.assetid: 48d54092-d055-449c-a409-829213db2989
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisOpenFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisOpenFile (NDIS 5.1)) in Windows   Vista. Supported for NDIS 5.1 drivers (see    NdisOpenFile (NDIS 5.1)) in Windows   XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOpenFile
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisOpenFile function



## -description
<p>The
  <b>NdisOpenFile</b> function returns a handle for an opened file.</p>


## -syntax

````
VOID NdisOpenFile(
  _Out_ PNDIS_STATUS          Status,
  _Out_ PNDIS_HANDLE          FileHandle,
  _Out_ PUINT                 FileLength,
  _In_  PNDIS_STRING          FileName,
  _In_  NDIS_PHYSICAL_ADDRESS HighestAcceptableAddress
);
````


## -parameters
<dl>

### -param <i>Status</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns the status of the open file
     operation, which can be one of the following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The handle at 
       <i>FileHandle</i> is valid for a subsequent call to 
       <b>NdisMapFile</b>.</p>
</dd>

### -param <a id="NDIS_STATUS_FILE_NOT_FOUND"></a><a id="ndis_status_file_not_found"></a>NDIS_STATUS_FILE_NOT_FOUND

<dd>
<p>The given string at 
       <i>FileName</i> did not specify a name found in the system object namespace.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>NDIS could not allocate the resources it needed to open the file and allocate a buffer for the
       file contents.</p>
</dd>

### -param <a id="NDIS_STATUS_ERROR_READING_FILE"></a><a id="ndis_status_error_reading_file"></a>NDIS_STATUS_ERROR_READING_FILE

<dd>
<p>The specified file's data could not be read into system memory for subsequent access by the
       caller.</p>
</dd>
</dl>
</dd>

### -param <i>FileHandle</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns the handle of the opened
     file if the call succeeds.</p>
</dd>

### -param <i>FileLength</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function writes the number of bytes of data
     in the opened file if the call succeeds.</p>
</dd>

### -param <i>FileName</i> [in]

<dd>
<p>A pointer to an NDIS_STRING type containing an initialized counted string, in the system-default
     character set, naming the file to be opened. For Windows 2000 and later drivers, this string contains
     Unicode characters. That is, for Windows 2000 and later, NDIS defines the NDIS_STRING type as a 
     <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> type.</p>
</dd>

### -param <i>HighestAcceptableAddress</i> [in]

<dd>
<p>The highest physical address in which the file data can be stored, or specifies -1 if the driver
     places no restrictions.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisOpenFile</b> opens a disk file, typically a file the driver will later download to program an
    intelligent NIC. 
    <b>NdisOpenFile</b> also allocates storage to hold file contents for the driver's subsequent call to the 
    <a href="..\ndis\nf-ndis-ndismapfile.md">NdisMapFile</a> function.</p>

<p>A miniport driver should call 
    <b>NdisOpenFile</b> only from the 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.</p>

<p>When 
    <b>NdisOpenFile</b> returns, the miniport driver can access file data by calling 
    <b>NdisMapFile</b>. It can call the 
    <a href="..\ndis\nf-ndis-ndisunmapfile.md">NdisUnmapFile</a> function to page out the file
    so it does not consume resources unnecessarily while the driver is not accessing the file data. When
    finished using the file, 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> must call the
    
    <a href="..\ndis\nf-ndis-ndisclosefile.md">NdisCloseFile</a> function.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff553681">NdisOpenFile (NDIS 5.1)</a>) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisOpenFile (NDIS 5.1)</b>) in Windows
   XP.</p>
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
<p>PASSIVE_LEVEL</p>
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
<a href="..\ndis\nf-ndis-ndisclosefile.md">NdisCloseFile</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismapfile.md">NdisMapFile</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisunmapfile.md">NdisUnmapFile</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisOpenFile function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
