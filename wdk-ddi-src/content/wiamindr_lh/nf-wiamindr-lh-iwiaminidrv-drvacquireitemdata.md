---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvAcquireItemData
title: IWiaMiniDrv::drvAcquireItemData
author: windows-driver-content
description: The IWiaMiniDrv::drvAcquireItemData method is called by the WIA service to transfer data from the device to an application.
old-location: image\iwiaminidrv_drvacquireitemdata.htm
old-project: image
ms.assetid: ab49643b-ab77-49ea-9a3b-e3a184cd29d0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWiaMiniDrv, drvAcquireItemData, IWiaMiniDrv::drvAcquireItemData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrv.drvAcquireItemData
req.alt-loc: wiamindr_lh.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IWiaMiniDrv
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvAcquireItemData method



## -description
<p>The <b>IWiaMiniDrv::drvAcquireItemData</b> method is called by the WIA service to transfer data from the device to an application.</p>


## -syntax

````
HRESULT drvAcquireItemData(
  [in]      BYTE                      *pWiasContext,
  [in]      LONG                      lFlags,
  [in, out] PMINIDRV_TRANSFER_CONTEXT pmdtc,
  [out]     LONG                      *plDevErrVal
);
````


## -parameters
<dl>

### -param pWiasContext [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param lFlags [in]

<dd>
<p>Is currently unused. </p>
</dd>

### -param pmdtc [in, out]

<dd>
<p>Points to a <a href="..\wiamindr_lh\ns-wiamindr-lh--minidrv-transfer-context.md">MINIDRV_TRANSFER_CONTEXT</a> structure containing the device transfer context. The MINIDRV_TRANSFER_CONTEXT structure contains parameters that pertain to the data to be transferred.</p>
</dd>

### -param plDevErrVal [out]

<dd>
<p>Points to a memory location that will receive a status code for this method. If this method returns S_OK, the value stored will be zero. Otherwise, a minidriver-specific error code will be stored at the location pointed to by this parameter.</p>
</dd>
</dl>

## -returns
<p>On success, the method should return S_OK and clear the device error value pointed to by <b>plDevErrVal</b>. If the transfer was canceled, the method should return S_FALSE. If the method fails, it should return a standard COM error code and fill in a minidriver-specific error code value in the memory pointed to by <b>plDevErrVal</b>. The <b>Remarks</b> section has additional return-value information that applies to ADF scanning.</p>

## -remarks
<p>There are two main types of transfer: memory-based, and file-based. The WIA service indicates which type is to be performed by the setting of <i>pmdtc</i>--&gt;<b>tymed</b>, which will be TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK for memory-based transfers, and TYMED_FILE or TYMED_MULTIPAGE_FILE for file transfers. For more information about these constants, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551656">WIA_IPA_TYMED</a>.</p>

<p>For memory-based transfers, a buffer may or may not have already been allocated, as indicated by the value in <i>pmdtc</i>--&gt;<b>bClassDrvAllocBuf</b>. The WIA service can pass up to two buffers to the minidriver, but typically passes only one. The number of buffers is specified by the value in <i>pmdtc</i>--&gt;<b>lNumBuffers</b>. If memory for the buffer is not already allocated, the minidriver should allocate it using any of the usual means, such as <b>CoTaskMemAlloc</b>, (described in the Windows SDK documentation), or <b>new</b>. If the minidriver allocates a buffer, it also has the responsibility of freeing the buffer.</p>

<p>For file transfers, the minidriver should first write the data to the buffer passed in the WIA service's call to this method, and then call <a href="..\wiamdef\nf-wiamdef-wiaswritepagebuftofile.md">wiasWritePageBufToFile</a> to write the buffer data to the file involved. The minidriver should not attempt to use the file handle specified in <b>pmdtc</b>--&gt;<b>hFile</b> to write the data to the file.</p>

<p>Periodically, the minidriver should call the <a href="image.iwiaminidrvcallback_minidrvcallback">IWiaMiniDrvCallBack::MiniDrvCallback</a> method in the COM interface point to by <i>pdmtc</i>--&gt;<b>pIWiaMiniDrvCallBack</b> to update the status of the transfer. For memory-based transfers, this function is used to pass the data back to the application. How often this function should be called is left to the minidriver, but it should be called about ten times, or roughly once per second during the transfer, whichever is more often.</p>

<p>Other transfer parameters that the WIA service provides include the following:</p>

<p><b>pmdtc</b>--&gt;<b>guidFormatID</b> - the data format</p>

<p><b>pmdtc</b>--&gt;<b>lCompression</b> - the type of compression used</p>

<p>A potential problem for ADF-equipped scanners is running out of paper during a scan operation. The HRESULT that your implementation of <b>IWiaMiniDrv::drvAcquireItemData</b> returns depends on the current setting of the scanner's WIA_DPS_PAGES property, and whether all pages were properly scanned. Use the following rules to guide you in determining the appropriate HRESULT to return in this method.</p>

<p>The WIA_DPS_PAGES property was set to 0, and the scanner emptied its ADF with no errors.</p>

<p>The WIA_DPS_PAGES property was set to N (where N &gt; 0), and the scanner processed N pages with no errors.</p>

<p>S_OK</p>

<p>The WIA_DPS_PAGES property was set to N, and the scanner processed at least one page but ran out of paper before processing all N pages.</p>

<p>WIA_STATUS_END_OF_MEDIA</p>

<p>The scanner has unexpectedly detected multiple page feed, stopped scanning, and has set the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551386">WIA_DPS_DOCUMENT_HANDLING_STATUS</a> to MULTIPLE_FEED. </p>

<p>WIA_ERROR_MULTI_FEED </p>

<p>The scanner ran out of paper on the first scan, regardless of the setting of the WIA_DPS_PAGES property.</p>

<p>A paper jam or other error occurred during the scan operation.</p>

<p>Other error code</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiasgetimageinformation.md">wiasGetImageInformation</a>
</dt>
<dt>
<a href="image.iwiaminidrv_drvgetdeviceerrorstr">IWiaMiniDrv::drvGetDeviceErrorStr</a>
</dt>
<dt>
<a href="..\wiamindr_lh\ns-wiamindr-lh--minidrv-transfer-context.md">MINIDRV_TRANSFER_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvAcquireItemData method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
